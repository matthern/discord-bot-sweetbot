import discord
import responses
import requests
from PIL import Image
from io import BytesIO
from secrets import bot_api_key
from secrets import yt_api_key
import youtube_dl
from googleapiclient.discovery import build
import time

VOTING_PERIOD = 10

async def send_message(message, user_message, is_private):
    try:
        if user_message.startswith('!image'):
            # Split the message into a list of words
            words = user_message.split()

            # Check if there are enough words to extract the text values
            if len(words) < 3:
                return 'Please provide enough text values for the image.'

           
            #Tmultiple words input:

            text1 = ' '.join(words[1:]).split("|")[0]
            text2 = ' '.join(words[1:]).split("|")[1]

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

                  
             # !worth command to return a different meme
        if user_message.startswith('!worth'):
            # Split the message into a list of words
            words = user_message.split()

            # Check if there are enough words to extract the text value
            if len(words) < 2:
                return 'Please provide the text value for the image.'

            # Extract the text value from the message
            text = ' '.join(words[1:])

            # Construct the API URL with the text value
            url = f"https://frenchnoodles.xyz/api/endpoints/worthless/?text={text}"

            # Send a GET request to the API
            res = requests.get(url)

            # Check if the request was successful
            if res.status_code != 200:
                return 'Sorry, there was an error retrieving the image.'

            # Try to send the image as a Discord message, or print the error message if it's a JSON response. Also return as private message if command run as PM.
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

async def search_youtube(query):
    YOUTUBE_API_KEY = yt_api_key
    youtube = build("youtube", "v3", developerKey=YOUTUBE_API_KEY)

    request = youtube.search().list(
        part="id,snippet",
        type='video',
        q=query,
        videoDefinition='high',
        maxResults=1,
        fields="items(id(videoId),snippet(publishedAt,channelId,channelTitle,title,description))"
    )
    response = request.execute()
    return response["items"]



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
    # Don't respond to messages sent by the bot itself
    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
    # Get the username, message content, and channel of the message
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f'{username} said: "{user_message}" ({channel})')
     # Check if the message starts with '?'
        if user_message[0] == '?':
            # If it does, remove the '?' and send the message privately
            user_message = user_message[1:]
            await send_message(message, user_message, is_private=True)
        else:
            # If it doesn't, send the message publicly
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
     
            # Check if the message starts with "!yt"
        if message.content.startswith("!yt"):
        # Split the message into a list of words
            words = message.content.split()

        # Get the search query (everything after the !yt command)
            query = " ".join(words[1:])

        # Search YouTube for the query
            yt_results = await search_youtube(query)

        # Get the first result
            video = yt_results[0]

        # Get the URL of the video
            url = f"https://www.youtube.com/watch?v={video['id']['videoId']}"
            await message.channel.send(f"is this the vid?:{url}")
        # Join the voice channel
            #voice_channel = message.author.voice.channel
            #await voice_channel.connect()

        # Create a player object
            #player = await YTDLSource.from_url(url, loop=client.loop)
            #player = await YTDLSource.from_url(url, loop=client.loop, stream=True)


        # Start playing the audio
            
         #   voice_channel = discord.utils.get(client.guilds[0].channels, name='shopify-think-tank  ')
         #   await voice_channel.connect()
        # Check if the voice channel was found
          #  if voice_channel is not None:
        # Connect to the voice channel
           #     await voice_channel.connect()
           #     print('Connected to the voice channel')
           # else:
            #    print('Could not find the voice channel')
            #player = await YTDLSource.from_url(url, loop=client.loop)
            #player.start()
        
        

        if message.content.startswith('!vote'):
        # Get the options from the command arguments
            options = message.content.split()[1:]
          # Send the poll message
            poll_message = await message.channel.send(f'Which of the following options do you prefer?\n\n{" ".join(options)}')

        # Add reactions for each option
            for i, option in enumerate(options):
                await poll_message.add_reaction(f'{i + 1}\u20e3')

        # Create a dictionary to store the results
            poll_results = {option: 0 for option in options}

        # Create a set to store the users who have voted
            voters = set()

        # Set a flag to indicate when the voting period is over
            voting_period_over = False

        # Start a loop to collect responses
            while not voting_period_over:
            # Wait for a reaction to be added to the message
                reaction, user = await client.wait_for('reaction_add')

            # Check if the user has already voted
                if user not in voters:
                # Check if the reaction is one of the options
                    if str(reaction.emoji) in poll_results:
                    # Increment the vote count for the option
                        poll_results[str(reaction.emoji)] += 1

                # Add the user to the voters set
                    voters.add(user)

            # Check if the voting period is over
                if time.time() - poll_message.created_at.timestamp() > VOTING_PERIOD:
                    voting_period_over = True

        # Calculate the total number of votes
           # Calculate the total number of votes
            total_votes = sum(int(votes) for votes in poll_results.values())

# Check if there were any votes
            if total_votes == 0:
    # Send a message indicating that the poll did not receive any votes
                await message.channel.send('No votes were cast in this poll.')
            else:
    # Construct the results message
                results_message = f'Poll Results:\n\n'
                for option, votes in poll_results.items():
                    results_message += f'{option}: {votes} votes ({votes / total_votes:.2f}%)\n'

    # Send the results message
            await message.channel.send(results_message)

     
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
