import discord
import os
from discord.ext import commands

# --- TOKEN DESDE VARIABLE DE ENTORNO ---
TOKEN = os.environ.get("DISCORD_TOKEN")  # Debe estar en Railway

# --- CONFIGURACIÓN DE INTENTS ---
intents = discord.Intents.default()
intents.message_content = True  # Solo lo necesario

class DashboardBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="!", intents=intents)

    async def setup_hook(self):
        # Cargar todos los cogs dentro de ./cogs
        cog_folder = "./cogs"
        for archivo in os.listdir(cog_folder):
            if archivo.endswith(".py"):
                cog_name = archivo[:-3]
                try:
                    await self.load_extension(f"cogs.{cog_name}")
                    print(f"✅ Cog cargado: {archivo}")
                except Exception as e:
                    print(f"❌ Error al cargar {archivo}: {e}")
        
        # Sincronizar comandos de aplicación (/)
        await self.tree.sync()
        print("--- 🖥️ DASHBOARD ONLINE ---")

bot = DashboardBot()

@bot.event
async def on_ready():
    print(f'Conectado como: {bot.user}')
    await bot.change_presence(
        activity=discord.Activity(type=discord.ActivityType.watching, name="Sistema Central")
    )

if __name__ == "__main__":
    if not TOKEN:
        print("❌ ERROR: No se encontró DISCORD_TOKEN en las variables de entorno")
    else:
        bot.run(TOKEN)


@bot.event
async def on_ready():
    print(f'Conectado como: {bot.user}')
    # Estado: "Viendo Dashboard"
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Sistema Central"))

if __name__ == "__main__":

    bot.run(TOKEN)
