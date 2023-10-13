import discord
import requests
from discord.ext import commands
import weather
import responses
import json

#get api
tokens = open('config.json')
json_contents = json.load(tokens)
discord_key = json_contents['botToken']





async def send_message(message, user_message):
    try:
        response = responses.handle_response(user_message)
        await message.channel.send(response)

    #need to add more exceptions and ways to handle, probably should make the bot say something like "invalid input or something"
    except Exception as e:
        print(e)

def run_discord_bot():
    intents = discord.Intents.all()
    intents.message_content = True
    #bot will recognize commands with the .
    client = commands.Bot(command_prefix=".", intents = intents)

    @client.command()
    async def weatherAt(ctx, city):
        temp = weather.get_weather(city)
        if (temp == "No City Found"):
            await ctx.send(temp)
        #need different images for different weather
        match temp[1]:
            case 'Clear':
                file = discord.File("/Users/rjl12/Downloads/WeatherIcons/sun.png", filename = "image.png")
                embed = discord.Embed(title = "Weather: Sunny", description = "Degrees: " + temp[0])
                embed.set_image(url = "attachment://image.png")
                await ctx.send(file = file, embed = embed)
            case 'overcast clouds':
                file = discord.File("/Users/rjl12/Downloads/WeatherIcons/cloudy.png", filename = "image.png")
                embed = discord.Embed(title = "Weather: Cloudy", description = "Degrees: " + temp[0])
                embed.set_image(url = "attachment://image.png")
                await ctx.send(file = file, embed = embed)
            case 'few clouds':
                file = discord.File("/Users/rjl12/Downloads/WeatherIcons/partlycloudy.png", filename = "image.png")
                embed = discord.Embed(title = "Weather: Partly Cloudy", description = "Degrees: " + temp[0])
                embed.set_image(url = "attachment://image.png")
                await ctx.send(file = file, embed = embed)
            case 'Rain':
                file = discord.File("/Users/rjl12/Downloads/WeatherIcons/rainy.png", filename = "image.png")
                embed = discord.Embed(title = "Weather: Rainy", description = "Degrees: " + temp[0])
                embed.set_image(url = "attachment://image.png")
                await ctx.send(file = file, embed = embed)
            #case 'Haze':
            
            #case 'Mist':

        #await ctx.send(embed = embed)

    @client.command()
    async def time(ctx, city):
        date_and_time = weather.get_time(city)
        time_api = date_and_time.split(' ')
        embed = discord.Embed(title = "Time: " + time_api[2], description = "Idk ill put a picture here hopefully")
        await ctx.send(embed = embed)

    @client.command()
    async def shutdown(ctx):
        await ctx.send("Shutting down")
        await client.close()

    @client.command()
    async def hello(ctx):
        await ctx.send("Waku Waku")

    @client.command()
    async def olof(ctx):
        embed = discord.Embed(color = 0x00ff00)
        file = discord.File("/Users/rjl12/Downloads/bocchiolof.jpg", filename = "image.png")
        embed.set_image(url = "attachment://image.png")
        await ctx.send(file = file, embed = embed)

    @client.command()
    async def sadge(ctx):
        embed = discord.Embed()
        embed.set_image(url = "https://media.tenor.com/0qj0aqZ0nucAAAAC/anya-spy-x-family-anime-anya-crying.gif")
        await ctx.channel.send(embed = embed)
        


    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')
    
    '''
    @client.event
    async def on_message(message):

        #detects own message
        if message.author == client.user:
            return
        
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f'{username} said: "{user_message}" ({channel})')
        
        await send_message(message, user_message)
    '''
   
    
    client.run(discord_key)