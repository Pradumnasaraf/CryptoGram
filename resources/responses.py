import random
import slugs
from requests.sessions import Session
import os
import json
from dotenv import load_dotenv
load_dotenv()

coinAPI = os.environ.get('COIN_API_KEY')

url ='https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'

parameters={
    'slug':'',
}

headers ={
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': coinAPI
}

session = Session()
session.headers.update(headers)

greetList =['hi', 'hi there', 'hello', 'hey','hey there']

def allMessages(input_text):

    if input_text in greetList:
        randomGreet = random.choice(greetList)
        return randomGreet.capitalize()

    elif input_text in ('who are you', 'who are you?'):
        return "I am Finantial Bot"

    elif input_text in ("whatis btc", "whatis doge"):
        return 122
    
    else:
        return "I Don't understand you"

# userInputSlug - slug entered by the user
def slugValue (userInputSlug):
    if userInputSlug in slugs.allSlug:
        # All slugs are stored in slugs module
        parameters['slug'] = slugs.allSlug[userInputSlug][1]
        tickerId = slugs.allSlug[userInputSlug][0]
        return getSlugValue(tickerId)
    else:
        return "Ticker/Symbol:\nNot found try diffent one"
    
def getSlugValue(tickerId):
    try:
        response = session.get(url,params=parameters)
        Data = json.loads(response.text)['data'][tickerId]
        name = Data['name']
        price = Data['quote']['USD']['price']
        return f'Current {name} price:\n${round(price, 3)}'
    except:
        print("Error")

