import random
import requests

def get_response(message: str) -> str:
    p_message = message.lower()
   
    #array of words that will trigger certain responses
    
    gay_words = ['gay','nerds','butt','love','chris','terry','oi','wow','love','like','sweety']
    sweet_words = ['Hmmm','Back it up Terry','Nice!','Hommus Lovers :)','what THE!!!','good one','OK','Hmm does chris love boys']
    lols = ['oi no lols fancy boy','oi no lols butt man','oi dont be lollin','Oi no lols allowed','one more lol outta you and ban','reported','all reported']
    lol_in = ['lol','ha ha','haha','lel','lolz','lelz','lulz','hehe','keke','he he','heha']
    mike_man = ['mike','mick','michael']
    mike = ['mike oxmall reporting in','they call me mike....mikey ox','is that you mikey boy? mike oxmall i think']
    ligma_res = ['They call me Love LIggins','Oi Im big Liggy ya heard of me','What','dogs m8','oh hi cobbs :)']
    ligma = ['deez','ligma','dogs','cuns','cuz']
    rob = ['sweetbotboy,','reported','oi']
    xmas = ['merry','happy new year','xmas']
    
    if p_message == 'hello':
        return 'Shut the heck!'

    for word in ligma:
        if word in p_message:
            return random.choice(ligma_res)

    for word in xmas:
        if word in p_message:
            return 'Merry Xmas noob, Love Sweety xoxo'

    for word in rob:
        if word in p_message:
            return 'Oh hi rob :)'

    for word in mike_man:
        if word in p_message:
            return random.choice(mike)

    for word in gay_words:
        if word in p_message:
            return random.choice(sweet_words) 

    if message == '!roll':
        return str(random.randint(000, 999))

       
    if p_message == 'dota2':
        return 'You are a nerd'

    for word in lol_in:
        if word in p_message:
            return random.choice(lols)

    def get_help_message():
        message = "`Welcome to the SweetyBot help menu!`\n"
        message += "`Here are the available commands:`\n"
        message += "`!play song title: Search youtube for a song and plays in the voice channel you are in. (bit shitty)`\n"
        message += "`!stop, !pause and !resume also work`\n"
        message += "`!roll: Generates a random number between 0001 and 999.`\n"
        message += "`!image top text | bottom text: Creates a shitty meme with the specified top and bottom text.(thats a Pipe sign inbetween the text.)`\n"
        message += "`!worth top text: Creates a shittier meme with the specified top text.`\n"
        message += "`!pres any text: Creates a shittier meme with the specified text.`\n"
        message += "`!change any text: Creates an even shittier meme with the specified text.`\n"
        message += "`!yt search query: Returns a youtube video from your search string.`\n"
        message += "`? prefixed to your message will return command/message privately.`\n"
        message += "`\n`"
        message += "`Don't mention Ligma or Mike lol, or talk smack about Sweety.`\n" 
        message += "`\n`"
        message += "`Cheers Cobbs.`\n"
        
        return message

    if p_message == '!help':
        return get_help_message()



    

