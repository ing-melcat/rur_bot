import discord
from discord.ext import commands
from discord import app_commands
import os


# --- CONFIGURACIÓN DE IMÁGENES ---
BANNER_IMG = "https://imgur.com/a/mRKKqF5"
LOGO_IMG = "https://imgur.com/h2FHJHU"

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
        await interaction.message.delete()


class Interfaz(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="dashboard", description="Abre el panel de control visual")
    async def dashboard(self, interaction: discord.Interaction):
        embed = discord.Embed(title="🚀 SYSTEM CORE // Inicio", description="Cargando interfaz...", color=0x00e5ff)
        embed.set_image(url=BANNER_IMG)
        await interaction.response.send_message(embed=embed, view=MenuDashboard())

    # ---------- AUTOMATIZACIÓN DE ROL ----------
    @commands.Cog.listener()
    async def on_ready(self):
        # Asignar rol a todos los miembros existentes al iniciar
        for guild in self.bot.guilds:
            role = discord.utils.get(guild.roles, name=AUTO_ROLE_NAME)
            if role:
                for member in guild.members:
                    if role not in member.roles and not member.bot:
                        try:
                            await member.add_roles(role)
                            print(f"✔️ Rol '{role.name}' asignado a {member}")
                        except Exception as e:
                            print(f"❌ Error asignando rol a {member}: {e}")

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        # Asignar rol automáticamente al entrar
        role = discord.utils.get(member.guild.roles, name=AUTO_ROLE_NAME)
        if role and not member.bot:
            try:
                await member.add_roles(role)
                print(f"✔️ Rol '{role.name}' asignado a {member}")
            except Exception as e:
                print(f"❌ Error asignando rol a {member}: {e}")


async def setup(bot):
    await bot.add_cog(Interfaz(bot))