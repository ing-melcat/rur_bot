import discord
from discord.ext import commands
from discord import app_commands

# --- CONFIGURACIÓN DE IMÁGENES ---
BANNER_IMG = "https://i.imgur.com/0v0a8Nq.png"
LOGO_IMG = "https://i.imgur.com/4Jj5Z6K.png"

class MenuDashboard(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        # Botón de enlace externo
        self.add_item(discord.ui.Button(label="Web Oficial", style=discord.ButtonStyle.link, url="https://google.com", row=1))

    # --- PÁGINA 1: INICIO ---
    @discord.ui.button(label="Inicio", style=discord.ButtonStyle.primary, emoji="🏠", row=0)
    async def inicio(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(title="🚀 SYSTEM CORE // Inicio", description="Panel de control central.", color=0x00e5ff)
        embed.set_image(url=BANNER_IMG)
        await interaction.response.edit_message(embed=embed, view=self)

    # --- PÁGINA 2: PROYECTOS ---
    @discord.ui.button(label="Proyectos", style=discord.ButtonStyle.secondary, emoji="🛠️", row=0)
    async def proyectos(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(title="🛠️ I+D // Proyectos", description="Desarrollos en curso.", color=0x9b59b6)
        embed.add_field(name="Proyecto Atlas", value="Robótica ROS2.", inline=False)
        embed.set_thumbnail(url=LOGO_IMG)
        await interaction.response.edit_message(embed=embed, view=self)

    # --- PÁGINA 3: EQUIPO ---
    @discord.ui.button(label="Personal", style=discord.ButtonStyle.secondary, emoji="👥", row=0)
    async def equipo(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(title="👥 STAFF", description="Organigrama.", color=0x2ecc71)
        embed.add_field(name="CEO", value="Antonio", inline=True)
        embed.set_thumbnail(url=LOGO_IMG)
        await interaction.response.edit_message(embed=embed, view=self)

    # --- BOTÓN NUEVO: CERRAR (Row 1 para que salga abajo) ---
    @discord.ui.button(label="Cerrar Panel", style=discord.ButtonStyle.danger, emoji="✖️", row=1)
    async def cerrar(self, interaction: discord.Interaction, button: discord.ui.Button):
        # Esta línea borra el mensaje completo
        await interaction.message.delete()


class Interfaz(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="dashboard", description="Abre el panel de control visual")
    async def dashboard(self, interaction: discord.Interaction):
        embed = discord.Embed(title="🚀 SYSTEM CORE // Inicio", description="Cargando interfaz...", color=0x00e5ff)
        embed.set_image(url=BANNER_IMG)
        await interaction.response.send_message(embed=embed, view=MenuDashboard())

async def setup(bot):
    await bot.add_cog(Interfaz(bot))