import discord
import random
from discord import Permissions
from colorama import Fore, Style
import asyncio
import requests
from discord.ext import commands
import time
import random
import string

token = ""


bot = commands.Bot(command_prefix= ".")

@bot.command()
async def locateip(ctx, arg):
    data = requests.get("https://api.ipgeolocation.io/ipgeo?apiKey=puturkey&ip=" + arg).json()
    await ctx.send("Locating ip...")
    time.sleep(3)

    embed = discord.Embed(title="IP Location", description="ez", color=0x00ff00)
    embed.add_field(name="Country", value=data["country_name"], inline=False)
    embed.add_field(name="City", value=data["city"], inline=False)
    embed.add_field(name="State", value=data["state_prov"], inline=False)
    embed.add_field(name="IP", value=data["ip"], inline=False)
    embed.add_field(name="Latitude", value=data["latitude"], inline=False)
    embed.add_field(name="Longitude", value=data["longitude"], inline=False)
    embed.add_field(name="Timezone", value=data["time_zone"], inline=False)
    embed.add_field(name="Continent", value=data["continent_name"], inline=False)
 
    await ctx.send(embed=embed)




bot.run(token, bot=True)
