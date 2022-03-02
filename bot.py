import telegram
from telegram import *
from telegram.ext import *
import os
import responses
from dotenv import load_dotenv
load_dotenv()

TELEBOT_API_KEY = os.environ.get('TELE_BOT_API')

bot = telegram.Bot(token=TELEBOT_API_KEY)
updater = Updater(token=TELEBOT_API_KEY, use_context=True)

# Dispatcher
ud = updater.dispatcher

# /hello
# def hello(update:Update,context:CallbackContext):
#     context.bot.send_message(chat_id = update.effective_chat.id,text= f'{responses.greet()}')

# /start
def start(update, context):
    update.message.reply_text(f'Hello👋, {update.effective_user.first_name}, I am a DeFi Bot. I talk about Blockchain and Decentaized Finance realated stuff , Developed by @Pradumna_saraf')

# every message handler
def handleAllUserText(update, context):
    userText = str(update.message.text).lower()
    botResponse = responses.allMessages(userText)
    update.message.reply_text(botResponse)

# /myid
def myid(update:Update,CallbackContext):
    update.message.reply_text(f"@{update.effective_user.username}")

# # /myid
def price(update:Update,CallbackContext):
    slugPart = str(update.message.text).split()
    tickeValue = responses.slugValue(slugPart[1].lower())
    update.message.reply_text(tickeValue)

ud.add_handler(CommandHandler('start', start))
ud.add_handler(CommandHandler('myid', myid))
ud.add_handler(CommandHandler('price', price))
ud.add_handler(MessageHandler(Filters.text & (~Filters.command), handleAllUserText))

# For terminal purpose
print("Bot Started")

# Starting the bot
updater.start_polling()

# idle state
updater.idle()
