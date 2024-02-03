from openai import OpenAI
from dotenv import load_dotenv
import discord
import os
import responses as r

def run_bot():
    load_dotenv()
    TOKEN = os.getenv('DISCORD_TOKEN')
    client = OpenAI()
    intents = discord.Intents.default()
    intents.message_content = True
    discord_client = discord.Client(intents=intents)

    @discord_client.event
    async def on_ready():
        print(f"{discord_client.user} is online")

    @discord_client.event
    async def on_message(msg):
        if msg.author == discord_client.user:
            return
        
        response = r.create_response(client, msg.content)
        if response == 'none':
            return

        await msg.delete()
        await msg.channel.send(f"Your message has been filtered: {response}")

    discord_client.run(TOKEN)