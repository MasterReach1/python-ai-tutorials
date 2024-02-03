import discord
import responses as r
from openai import OpenAI
from dotenv import load_dotenv
import os

def run_bot():
    load_dotenv()
    DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
    intents = discord.Intents.default()
    intents.message_content = True
    discord_client = discord.Client(intents=intents)
    openai_client = OpenAI()

    @discord_client.event
    async def on_ready():
        print(f'{discord_client.user} is running properly!')

    @discord_client.event
    async def on_message(msg):
        if msg.author == discord_client.user:
            return
        
        response = r.create_response(openai_client, msg.content)

        if response == 'none':
            return
        
        await msg.delete()
        await msg.channel.send(f'Your message has been filtered for bad language: {response}')

    discord_client.run(DISCORD_TOKEN)