import logging
import discord
from discord import app_commands

logger = logging.getLogger("discord")


class CommandRegistry:
    def __init__(self, bot):
        self.bot = bot

    def _get_command_signature(self, command):
        command_type = getattr(command, 'type', discord.AppCommandType.chat_input)

        signature = {
            "name": command.name,
            "type": int(command_type.value),
            "description": getattr(command, 'description', ""),
            "options": []
        }

        if signature["type"] == 1:
            if hasattr(command, 'commands'):
                for sub_command in command.commands:
                    signature["options"].append(self._get_command_signature(sub_command))
            elif hasattr(command, '_params'):
                for param in command._params.values():
                    signature["options"].append({
                        "name": param.name,
                        "description": param.description,
                        "type": int(param.type.value),
                        "required": param.required
                    })

        signature["options"] = sorted(signature["options"], key=lambda x: x["name"])
        return signature

    async def get_sync_status(self, guild: discord.Guild = None):
        local_commands = self.bot.tree.get_commands(guild=guild)
        try:
            remote_commands = await self.bot.tree.fetch_commands(guild=guild)
        except Exception as e:
            logger.error(f"Dopamine Framework: Failed to fetch remote commands: {e}")
            return False

        if len(local_commands) != len(remote_commands):
            return False

        local_map = {c.name: self._get_command_signature(c) for c in local_commands}

        remote_map = {}
        for c in remote_commands:
            remote_map[c.name] = self._parse_remote_signature(c)

        return local_map == remote_map

    def _parse_remote_signature(self, command):
        options = []
        raw_options = getattr(command, 'options', [])

        for opt in raw_options:
            if opt.type.value in (1, 2):
                options.append(self._parse_remote_signature(opt))
            else:
                options.append({
                    "name": opt.name,
                    "description": opt.description,
                    "type": int(opt.type.value),
                    "required": getattr(opt, 'required', False)
                })

        return {
            "name": command.name,
            "type": int(command.type.value),
            "description": getattr(command, 'description', ""),
            "options": sorted(options, key=lambda x: x["name"])
        }

    async def smart_sync(self, guild: discord.Guild = None):
        is_synced = await self.get_sync_status(guild)

        scope = f"Guild({guild.id})" if guild else "Global"

        if not is_synced:
            logger.info(f"Dopamine Framework: Detected changes. Syncing {scope} commands...")
            await self.bot.tree.sync(guild=guild)
            return f"Dopamine Framework: {scope} commands synced successfully."
        else:
            logger.info(f"No changes detected for {scope}. Skipping sync.")
            return f"Dopamine Framework: {scope} commands are already up to date."

    async def force_sync(self, guild: discord.Guild = None):
        scope = f"Guild: {guild.name} ({guild.id})" if guild else "Global"
        try:
            await self.bot.tree.sync(guild=guild)
            return f"Dopamine Framework: Synced slash commands to: {scope}."
        except discord.HTTPException as e:
            return f"Dopamine Framework: Rate limit or API error: {e}"