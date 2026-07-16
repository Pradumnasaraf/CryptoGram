import os
import responses
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)
from dotenv import load_dotenv
load_dotenv()

TELEBOT_API_KEY = os.environ.get('TELE_BOT_API')

# /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'Hello👋, {update.effective_user.first_name}, I am a DeFi Bot. I talk about Blockchain and Decentaized Finance realated stuff , Developed by @Pradumna_saraf')

# every message handler
async def handleAllUserText(update: Update, context: ContextTypes.DEFAULT_TYPE):
    userText = str(update.message.text).lower()
    botResponse = responses.allMessages(userText)
    await update.message.reply_text(botResponse)

# /myid
async def myid(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"@{update.effective_user.username}")

# /price
async def price(update: Update, context: ContextTypes.DEFAULT_TYPE):
    slugPart = str(update.message.text).split()
    tickeValue = responses.slugValue(slugPart[1].lower())
    await update.message.reply_text(tickeValue)


def main():
    application = Application.builder().token(TELEBOT_API_KEY).build()

    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('myid', myid))
    application.add_handler(CommandHandler('price', price))
    application.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handleAllUserText))

    # For terminal purpose
    print("Bot Started")

    # Starting the bot
    application.run_polling()


if __name__ == '__main__':
    main()
