import random

def handle_response(message, private) -> str:
    p_message = message.lower()

    if private == True:
        if p_message == 'hello':
            return "Waku Waku"
    
        if p_message == 'roll':
            return str(random.randint(1,6))
    
        if p_message == "help":
            return "`This is a help message that you can modify`"
    else: 
        if p_message == '!hello':
            return "Waku Waku"
    
        if p_message == '!roll':
            return str(random.randint(1,6))
    
        if p_message == "!help":
            return "`!hello \n !help \n !roll`"
    