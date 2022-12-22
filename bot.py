import discord
import responses
import requests
from PIL import Image
from io import BytesIO
from secrets import bot_api_key

async def send_message(message, user_message, is_private):
    try:
        if user_message.startswith('!image'):
            # Split the message into a list of words
            words = user_message.split()

            # Check if there are enough words to extract the text values
            if len(words) < 3:
                return 'Please provide both text values for the image.'

            # Extract the text values from the message
            text1 = words[1]
            text2 = words[2]

            # Construct the API URL with the text values
            url = f"https://frenchnoodles.xyz/api/endpoints/drake/?text1={text1}&text2={text2}"

            # Send a GET request to the API
            res = requests.get(url)

            # Check if the request was successful
            if res.status_code != 200:
                return 'Sorry, there was an error retrieving the image.'

            # Try to send the image as a Discord message, or print the error message if it's a JSON response
            try:
                image = discord.File(BytesIO(res.content), filename='image.png')
                if is_private:
                    await message.author.send(file=image)
                else:
                    await message.channel.send(file=image)
            except:
                print(res.json())
                return 'Sorry, there was an error sending the image.'

            return 'Image sent!'

        else:
            response = responses.get_response(user_message)
            if is_private:
                await message.author.send(response)
            else:
                await message.channel.send(response)

    except Exception as e:
        print(e)


def run_discord_bot():
    TOKEN = bot_api_key
    intents = discord.Intents.default()
    intents.message_content = True
    intents.members = True
    intents.presences = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user.name} is now running!')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f'{username} said: "{user_message}" ({channel})')

        if user_message[0] == '?':
            user_message = user_message[1:]
            await send_message(message, user_message, is_private=True)
        else:
            await send_message(message, user_message, is_private=False)

        if 'happy birthday' in message.content.lower():
            await message.channel.send('🎈🎉 🎈🎉 Happy Birthday! 🎈🎉 🎈🎉')  
        
        if "!cun" in message.content:
        # Send the message "Hi (username)" to the channel
            await message.channel.send(f"Hi {message.author.mention}")
        if "sweety" in message.content:
        # Send the message "shut it (username)" to the channel
            await message.channel.send(f"shut it {message.author.mention}, u cun")
        if "fuck" in message.content:
        # Send the message "Hey hold up (username)" to the channel
            await message.channel.send(f"Hey hold up there fellow {message.author.mention}, ur a bitch :D")
     
           

    @client.event
    async def on_member_join(member):
    # Send the message "Hello (username)" to the channel
        await member.guild.default_channel.send(f"Hey Cobba: {member.mention}, welcome m8")
                   
    #annoyed my discord friends too much :D
    #@client.event
    #async def on_presence_update(before, after):
    # Check if the user's status has changed to "online"
    #    try:
    #        print(f"before.status: {before.status}")
    #        print(f"after.status: {after.status}")
    #        if before.status != after.status and after.status == discord.Status.online:
        # Get the general channel
    #            text_channel = after.guild.text_channels[0]
        # Send the message "Hello (username)" to the channel
    #            await text_channel.send(f"Hello {after.mention}, Welcome back online cobbs. Kind Regards: SBB (`SweetBotBoy`)")
    #    except Exception as e:
        # Print the error message
    #        print(e)        

    client.run(TOKEN)
