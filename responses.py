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
    
    if p_message == 'hello':
        return 'Shut the heck!'

    for word in ligma:
        if word in p_message:
            return random.choice(ligma_res)

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

    if p_message == '!help':
        return '`Type !roll for a number 0001 to 999. Dont u fkn talk about Ligma or Mike lol. Type:!image word1 word2 to make a shitty meme. Cheers cobbs`'
    
    if p_message == 'dota2':
        return 'You are a nerd'

    for word in lol_in:
        if word in p_message:
            return random.choice(lols)



    

