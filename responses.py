import random
import weather

def handle_response(message) -> str:
    p_message = message.lower()

    if p_message == '!hello':
        return "Waku Waku"
    
    elif p_message == '!roll':
        return str(random.randint(1,6))
    
    elif p_message == "!help":
        return "`!hello \n !help \n !roll`"
        
    elif "!weather" in p_message:
        split = p_message.split(' ', 1)
        city = split[1]
        return weather.get_weather(city)
        
    elif "!time" in p_message:
        split = p_message.split(' ', 1)
        city = split[1]
        date_and_time = weather.get_time(city).split(' ')
        return date_and_time[1]