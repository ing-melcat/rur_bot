import discord
import os
from discord.ext import commands

TOKEN = os.environ["DISCORD_TOKEN"]
AUTO_ROLE_NAME = os.environ.get("AUTO_ROLE_NAME", "Miembro")

intents = discord.Intents.default()
intents.guilds = True
intents.members = True  # NECESARIO para auto-rol

class DashboardBot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix="!",
            intents=intents
        )

    async def setup_hook(self):
        # Cargar cogs
        for file in os.listdir("./cogs"):
            if file.endswith(".py"):
                await self.load_extension(f"cogs.{file[:-3]}")
                print(f"✅ Cargado: {file}")

        await self.tree.sync()
        print("🚀 Bot listo")

bot = DashboardBot()

@bot.event
async def on_ready():
    print(f"🟢 Conectado como {bot.user}")

    # Asignar rol a usuarios existentes
    for guild in bot.guilds:
        role = discord.utils.get(guild.roles, name=AUTO_ROLE_NAME)
        if not role:
            print(f"⚠️ Rol '{AUTO_ROLE_NAME}' no existe en {guild.name}")
            continue

        for member in guild.members:
            if not member.bot and role not in member.roles:
                try:
                    await member.add_roles(role)
                except:
                    pass

@bot.event
async def on_member_join(member):
    role = discord.utils.get(member.guild.roles, name=AUTO_ROLE_NAME)
    if role:
        await member.add_roles(role)

bot.run(TOKEN)