import logging
import discord
import hashlib
import json
from discord import app_commands

logger = logging.getLogger("discord")


class CommandRegistry:
    def __init__(self, bot):
        self.bot = bot

    def _get_clean_signature(self, command, is_remote=False):

        if is_remote:
            cmd_type = int(command.type.value)
        elif isinstance(command, discord.app_commands.ContextMenu):
            cmd_type = command.type.value
        else:
            cmd_type = 1

        description = getattr(command, 'description', "") or ""
        if cmd_type in (2, 3):
            description = ""

        signature = {
            "name": str(command.name),
            "type": cmd_type,
            "description": str(description),
            "options": []
        }

        if cmd_type == 1:
            raw_options = []
            if is_remote:
                raw_options = getattr(command, 'options', [])
            else:
                if hasattr(command, 'commands'):
                    raw_options = command.commands
                elif hasattr(command, '_params'):
                    raw_options = command._params.values()

            for opt in raw_options:
                if is_remote:
                    if int(opt.type.value) in (1, 2):
                        signature["options"].append(self._get_clean_signature(opt, is_remote=True))
                    else:
                        signature["options"].append({
                            "name": str(opt.name),
                            "description": str(opt.description or ""),
                            "type": int(opt.type.value),
                            "required": getattr(opt, 'required', False)
                        })
                else:
                    if isinstance(opt, (discord.app_commands.Command, discord.app_commands.Group)):
                        signature["options"].append(self._get_clean_signature(opt, is_remote=False))
                    else:
                        signature["options"].append({
                            "name": str(opt.name),
                            "description": str(opt.description or ""),
                            "type": int(opt.type.value),
                            "required": getattr(opt, 'required', True)
                        })

        signature["options"] = sorted(signature["options"], key=lambda x: x["name"])
        return signature

    def _generate_hash(self, command_map):
        sorted_map = {k: command_map[k] for k in sorted(command_map.keys())}
        dump = json.dumps(sorted_map, sort_keys=True)
        return hashlib.sha256(dump.encode('utf-8')).hexdigest()

    async def get_sync_status(self, guild: discord.Guild = None):
        local_commands = self.bot.tree.get_commands(guild=guild)
        try:
            remote_commands = await self.bot.tree.fetch_commands(guild=guild)
        except Exception as e:
            logger.error(f"Dopamine Framework: Failed to fetch: {e}")
            return False

        if len(local_commands) != len(remote_commands):
            return False

        local_map = {c.name: self._get_clean_signature(c, is_remote=False) for c in local_commands}
        remote_map = {c.name: self._get_clean_signature(c, is_remote=True) for c in remote_commands}

        local_hash = self._generate_hash(local_map)
        remote_hash = self._generate_hash(remote_map)

        if local_hash != remote_hash:
            logger.debug(f"Local Hash: {local_hash}")
            logger.debug(f"Remote Hash: {remote_hash}")

        return local_hash == remote_hash

    async def smart_sync(self, guild: discord.Guild = None):
        is_synced = await self.get_sync_status(guild)
        scope = f"Guild({guild.id})" if guild else "Global"

        if not is_synced:
            logger.info(f"Dopamine Framework: Detected changes. Syncing {scope} commands...")
            await self.bot.tree.sync(guild=guild)
            return f"Dopamine Framework: Detected changes, completed {scope} commands sync successfully."

        logger.info(f"No changes detected for {scope}. Skipping sync.")
        return f"Dopamine Framework: {scope} commands are already up to date."

    async def force_sync(self, guild: discord.Guild = None):
        scope = f"Guild: {guild.name} ({guild.id})" if guild else "Global"
        try:
            await self.bot.tree.sync(guild=guild)
            return f"Dopamine Framework: Synced slash commands to: {scope}."
        except discord.HTTPException as e:
            return f"Dopamine Framework: Rate limit or API error: {e}"