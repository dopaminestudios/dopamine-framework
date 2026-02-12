import logging
import discord
from discord import app_commands

logger = logging.getLogger("discord")


class CommandRegistry:
    def __init__(self, bot):
        self.bot = bot

    def _get_command_signature(self, command):
        signature = {
            "name": command.name,
            "description": command.description,
            "options": []
        }

        if hasattr(command, 'parameters'):
            for param in command.parameters:
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
            logger.error(f"Failed to fetch remote commands: {e}")
            return False

        if len(local_commands) != len(remote_commands):
            return False

        local_map = {c.name: self._get_command_signature(c) for c in local_commands}

        remote_map = {}
        for c in remote_commands:
            remote_map[c.name] = {
                "name": c.name,
                "description": c.description,
                "options": sorted([
                    {
                        "name": opt.name,
                        "description": opt.description,
                        "type": int(opt.type.value),
                        "required": opt.required
                    } for opt in c.options
                ], key=lambda x: x["name"]) if c.options else []
            }

        return local_map == remote_map

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