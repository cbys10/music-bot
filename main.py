import discord
from discord.ext import commands
from discord.utils import get
import youtube_dl

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command()
async def join(ctx, Lobby):
    voice_channel = discord.utils.get(ctx.guild.voice_channels, name=Lobby)
    if voice_channel is None:
        voice_channel = discord.utils.get(ctx.guild.voice_channels, id=int(Lobby))

    if voice_channel is not None:
        voice_client = get(bot.voice_clients, guild=ctx.guild)

        if voice_client and voice_client.is_connected():
            await voice_client.move_to(voice_channel)
        else:
            voice_client = await voice_channel.connect()
    else:
        await ctx.send('Voice channel not found.')


@bot.command()
async def play(ctx):
    if ctx.author.voice is None or ctx.author.voice.channel is None:
        await ctx.send("You need to be in a voice channel to use this command.")
        return

    voice_channel = ctx.author.voice.channel
    voice_client = get(bot.voice_clients, guild=ctx.guild)

    if voice_client and voice_client.is_connected():
        if voice_client.channel == voice_channel:
            await ctx.send("The bot is already connected to your voice channel.")
            return
        else:
            await voice_client.move_to(voice_channel)
    else:
        voice_client = await voice_channel.connect()

    file_path = "phonk.mp3"  # Replace with the actual file path

    voice_client.play(discord.FFmpegPCMAudio(file_path))


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

bot.run('MTEzMDM0MTczMjMwMzc2NTYxNA.GHCam_.XjyYDZ9E8la6GK3dBi7Bjs7fmCH3A3Wes3QQhI')