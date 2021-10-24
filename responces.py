def sample_response(input_text):
    
    user_message = str(input_text).lower()

    if user_message in ('hey', 'hello', 'sup'):
        return "Hey! How's it going?"

    if user_message in ('who are you', 'who are you?'):
        return "I am Finantial Bot"
    
    return "I Don't understand you"


