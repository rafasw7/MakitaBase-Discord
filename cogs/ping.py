import discord
from discord.ext import commands
import time
import platform
import random
import asyncio

class PingView(discord.ui.View):
    def __init__(self, bot):
        super().__init__(timeout=None)
        self.bot = bot
        self.start_time = time.time()

    async def update_ping_embed(self, interaction):
        current_time = time.time()
        uptime_seconds = int(current_time - self.start_time)
        hours = uptime_seconds // 3600
        minutes = (uptime_seconds % 3600) // 60
        seconds = uptime_seconds % 60
        latency = round(self.bot.latency * 1000)

        speed_emojis = ["⚡", "💨", "🚀", "🔥", "💫", "🏎️"]
        speed_emoji = random.choice(speed_emojis)

        if latency <= 100:
            color = discord.Color.green()
            ping_status = "🟢 Suave como manteiga!"
        elif latency <= 300:
            color = discord.Color.yellow()
            ping_status = "🟡 Tá de boa, meio sonolento..."
        else:
            color = discord.Color.red()
            ping_status = "🔴 Ih rapaz... parece que travou 😅"

        ping_bar = "▰" * min(latency // 50, 10) + "▱" * (10 - min(latency // 50, 10))

        embed = discord.Embed(
            title=f"{speed_emoji} P I N G - S T A T U S",
            description="📶 Atualizando status do bot em tempo real...",
            color=color
        )
        embed.add_field(name="📡 Latência", value=f"**{latency} ms**\n{ping_bar}", inline=False)
        embed.add_field(name="🐍 Python", value=f"**{platform.python_version()}**", inline=True)
        embed.add_field(name="⏰ Uptime", value=f"**{hours}h {minutes}m {seconds}s**", inline=True)
        embed.add_field(name="💭 Status", value=f"{ping_status}", inline=False)
        embed.set_footer(text=f"Makita Bot 💻 | Feito com 💙 por Rafasw7")

        await interaction.response.edit_message(embed=embed, view=self)

    @discord.ui.button(label="Repetir Teste", style=discord.ButtonStyle.blurple, emoji="🔄", custom_id="refresh_ping")
    async def repeat_ping(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.defer(thinking=True)
        await asyncio.sleep(0.8)
        await self.update_ping_embed(interaction)

    @discord.ui.button(label="Fechar", style=discord.ButtonStyle.red, emoji="❌", custom_id="close_ping")
    async def close_ping(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(
            title="🛑 Teste Encerrado",
            description=f"O status do bot foi fechado por **{interaction.user.display_name}**.",
            color=discord.Color.red()
        )
        await interaction.response.edit_message(embed=embed, view=None)


class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.start_time = time.time()

    @commands.command(name="ping")
    async def ping(self, ctx):
        current_time = time.time()
        uptime_seconds = int(current_time - self.start_time)
        hours = uptime_seconds // 3600
        minutes = (uptime_seconds % 3600) // 60
        seconds = uptime_seconds % 60
        latency = round(self.bot.latency * 1000)

        speed_emojis = ["⚡", "💨", "🚀", "🔥", "💫", "🏎️"]
        speed_emoji = random.choice(speed_emojis)

        if latency <= 100:
            color = discord.Color.green()
            ping_status = "🟢 Suave como manteiga!"
        elif latency <= 300:
            color = discord.Color.yellow()
            ping_status = "🟡 Tá de boa, meio sonolento..."
        else:
            color = discord.Color.red()
            ping_status = "🔴 Ih rapaz... parece que travou 😅"

        ping_bar = "▰" * min(latency // 50, 10) + "▱" * (10 - min(latency // 50, 10))

        embed = discord.Embed(
            title=f"{speed_emoji} P I N G - S T A T U S",
            description="📶 Status atual do bot em tempo real ⚙️",
            color=color
        )
        embed.add_field(name="📡 Latência", value=f"**{latency} ms**\n{ping_bar}", inline=False)
        embed.add_field(name="🐍 Python", value=f"**{platform.python_version()}**", inline=True)
        embed.add_field(name="⏰ Uptime", value=f"**{hours}h {minutes}m {seconds}s**", inline=True)
        embed.add_field(name="💭 Status", value=f"{ping_status}", inline=False)
        embed.set_author(name=f"{ctx.author.display_name}", icon_url=ctx.author.display_avatar)
        embed.set_footer(text=f"Makita Bot 💻 | Feito com 💙 por Rafasw7")

        view = PingView(self.bot)
        await ctx.send(embed=embed, view=view)

async def setup(bot):
    await bot.add_cog(Ping(bot))