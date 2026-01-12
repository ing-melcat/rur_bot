import discord
from discord.ext import commands
import asyncio

class Bot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()  # 🚫 SIN message_content
        super().__init__(
            command_prefix="!",  # no se usa, pero discord.py lo pide
            intents=intents
        )

    async def setup_hook(self):
        # Sync global de slash commands
        await self.tree.sync()
        print("✅ Slash commands sincronizados")

bot = Bot()

@bot.event
async def on_ready():
    print(f"🤖 Bot listo como {bot.user}")

# ===== SLASH COMMAND =====
@bot.tree.command(name="ping", description="Ping del bot")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message("🏓 Pong")

bot.run("TU_TOKEN")