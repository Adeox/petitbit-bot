import discord
from discord.ext import tasks
import os
from datetime import datetime

intents = discord.Intents.default()
client = discord.Client(intents=intents)

CHANNEL_ID = 1378049748975751332  # Remplace si besoin

@client.event
async def on_ready():
    print(f"{client.user} est connecté !")
    daily_message.start()

@tasks.loop(minutes=1)
async def daily_message():
    now = datetime.now()
    if now.hour == 10 and now.minute == 0:
        channel = client.get_channel(CHANNEL_ID)
        if channel:
            await channel.send("👋 Coucou ! PetitBit est là pour t’aider à apprendre le langage Python aujourd’hui ! 💡")

TOKEN = os.getenv("DISCORD_TOKEN")
client.run(TOKEN)
