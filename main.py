import discord
import os
from discord.ext import commands

# --- PON TU TOKEN AQUÍ ---
TOKEN = ""

# Configuración
intents = discord.Intents.default()
intents.message_content = True

class DashboardBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="!", intents=intents)

    async def setup_hook(self):
        # Carga solo lo que haya en la carpeta cogsT
        for archivo in os.listdir('./cogs'):
            if archivo.endswith('.py'):
                try:
                    await self.load_extension(f'cogs.{archivo[:-3]}')
                    print(f"✅ Interfaz cargada: {archivo}")
                except Exception as e:
                    print(f"❌ Error: {e}")
        
        # Sincroniza el menú de comandos '/'
        await self.tree.sync()
        print("--- 🖥️ DASHBOARD ONLINE ---")

bot = DashboardBot()

@bot.event
async def on_ready():
    print(f'Conectado como: {bot.user}')
    # Estado: "Viendo Dashboard"
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Sistema Central"))

if __name__ == "__main__":
    bot.run(TOKEN)