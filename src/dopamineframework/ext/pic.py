import discord
from discord import app_commands
from discord.ext import commands
from ..core.dashboard import OwnerDashboard

class Pic(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="od", description=".")
    @app_commands.describe(ephemeral="Set to True so that only you can see the dashboard message.")
    async def zc(self, interaction: discord.Interaction, ephemeral: bool = False):
        if not await self.bot.is_owner(interaction.user):
            await interaction.response.send_message("🤫", ephemeral=True)
            return
        view = OwnerDashboard(self.bot, interaction.user)
        await interaction.response.send_message(view=view, ephemeral=True if ephemeral else False)


async def setup(bot):
    await bot.add_cog(Pic(bot))