import discord
import os
from discord.ext import commands

TOKEN = os.environ["BOT_TOKEN"]
CHANNEL_ID = int(os.environ["CHANNEL_ID"])
ROLE_NAME = os.environ["AUTO_ROLE_NAME"]

intents = discord.Intents.default()
intents.members = True  # ← NECESARIO para autoroles (solo este)

class DashboardBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="!", intents=intents)

    async def setup_hook(self):
        await self.load_extension("cogs.interfaz")
        print("✅ Interfaz cargada")

bot = DashboardBot()

@bot.event
async def on_ready():
    print(f"🟢 Conectado como {bot.user}")

    # -------- DASHBOARD AUTOMÁTICO --------
    channel = bot.get_channel(CHANNEL_ID)
    if channel:
        async for msg in channel.history(limit=20):
            if msg.author == bot.user:
                await msg.delete()

        from cogs.interfaz import send_dashboard
        await send_dashboard(channel)

    # -------- AUTO-ROL A LOS YA EXISTENTES --------
    for guild in bot.guilds:
        role = discord.utils.get(guild.roles, name=ROLE_NAME)
        if not role:
            print(f"❌ Rol '{ROLE_NAME}' no existe en {guild.name}")
            continue

        for member in guild.members:
            if not member.bot and role not in member.roles:
                try:
                    await member.add_roles(role)
                except:
                    pass

@bot.event
async def on_member_join(member):
    role = discord.utils.get(member.guild.roles, name=ROLE_NAME)
    if role:
        await member.add_roles(role)

bot.run(TOKEN)