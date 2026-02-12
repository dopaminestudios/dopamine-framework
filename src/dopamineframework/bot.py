import os
import time
import signal
import asyncio
import logging
import discord
from discord import app_commands
from discord.ext import commands
from .utils.log import LoggingManager
from .core.commands_registry import CommandRegistry
from .ext.path import framework_version
import os
import sys

logger = logging.getLogger("discord")


class Bot(commands.Bot):
    def __init__(self, cogs_path: str = "cogs", log_path: str = None, default_diagnostics: bool = True, *args, **kwargs):
        command_prefix = kwargs.pop("command_prefix", "!")

        super().__init__(
            command_prefix=command_prefix,
            help_command=None,
            member_cache_flags=discord.MemberCacheFlags(voice=True, joined=False),
            chunk_guilds_at_startup=False,
            guild_ready_timeout=0,
            *args, **kwargs
        )
        self.cogs_path = cogs_path
        self.log_path = log_path
        self.process_start_time = time.time()
        self.default_diagnostics = default_diagnostics
        self.registry = CommandRegistry(self)
        self.start_time = None

    async def setup_hook(self):
        if self.log_path:
            try:
                self.logger = LoggingManager(self.log_path)
            except Exception as e:
                logger.error(f"Failed to initialize logging manager: {e}")

        if os.path.exists(self.cogs_path):
            base_module = self.cogs_path.replace(os.path.sep, ".").strip(".")

            for filename in os.listdir(self.cogs_path):
                if filename.endswith(".py") and not filename.startswith("__"):
                    extension = f"{base_module}.{filename[:-3]}"
                    try:
                        await self.load_extension(extension)
                        print(f"> Loaded {extension} Successfully")
                    except Exception as e:
                        print(f"ERROR: Failed to load {extension}: {e}")
        else:
            print(f"WARNING: '{self.cogs_path}' directory not found.")
        if self.default_diagnostics:
            await self.load_extension("dopamineframework.ext.diagnostics")
        status = await self.registry.smart_sync()
        print(status)

        for s in (signal.SIGINT, signal.SIGTERM):
            self.loop.add_signal_handler(
                s, lambda: asyncio.create_task(self.signal_handler())
            )

    async def signal_handler(self):
        print("\nBot shutdown requested...")
        extensions = list(self.extensions.keys())
        for extension in extensions:
            try:
                await self.unload_extension(extension)
                print(f"> Unloaded {extension} successfully")
            except Exception as e:
                print(f"Error unloading {extension}: {e}")

        print("👋 Goodbye!")
        await self.close()

    async def restart_bot(self):
        print()
        print("Restarting bot...")
        await self.signal_handler()
        os.execv(sys.executable, [sys.executable] + sys.argv)

    async def on_ready(self):
        if self.owner_id is None:
            app_info = await self.application_info()
            if app_info.team:
                self.owner_id = app_info.team.owner_id
            else:
                self.owner_id = app_info.owner.id

        owner_user = self.get_user(self.owner_id) or await self.fetch_user(self.owner_id)
        owner_user_name = owner_user.name

        banner = ("\n"
                  f"---------------------------------------------------\n"
                  f"Powered by Dopamine Framework v{framework_version}\n"
                  "\n"
                  f"Bot ready: {self.user} (ID: {self.user.id})\n"
                  f"Bot Owner identified: {owner_user_name}\n"
                  f"---------------------------------------------------\n"
                  "")

        print(banner)


        self.start_time = time.time()