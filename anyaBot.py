import discord
from discord.ext import commands
import responses
import json

#get api
tokens = open('config.json')
json_contents = json.load(tokens)
api_key = json_contents['botToken']



async def send_message(message, user_message):
    try:
        response = responses.handle_response(user_message)
        await message.channel.send(response)

    #need to add more exceptions and ways to handle, probably should make the bot say something like "invalid input or something"
    except Exception as e:
        print(e)

def run_discord_bot():
    intents = discord.Intents.default()
    intents.message_content = True
    client = commands.Bot(command_prefix='.', intents = discord.Intents.all())


    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')


    @client.event
    async def on_message(message):

        #detects own message
        if message.author == client.user:
            return
        
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)
        
        '''does not work idk why want to implement a shutdown
        
        if user_message is ".shutdown":
            async def shutdown(ctx):
                await ctx.send("Shutting down")
                await client.close()
        '''

        print(f'{username} said: "{user_message}" ({channel})')
        
        await send_message(message, user_message)
    
    client.run(api_key)