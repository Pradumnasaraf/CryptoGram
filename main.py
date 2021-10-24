from telegram.ext import Updater, CommandHandler , MessageHandler, Filters
import responces as R

API_KEY = ''

print("Bot Started")

def handle_message(update, context):
    text = str(update.message.text).lower()
    response = R.sample_response(text)
    update.message.reply_text(response)

def start_command(update, context):
    update.message.reply_text('''
Hey!, I am finance Bot!
Develpod By: @Pradumna_saraf
''')

def help_command(update, context):
    update.message.reply_text("If you need help! you should ask for it on Google!")


def error(update, context):
    print(f"update {update} caused error {context.error}")

def main():
    updater = Updater(API_KEY, use_context = True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start_command))

    dp.add_handler(CommandHandler("help", help_command))

    dp.add_handler(MessageHandler(Filters.text, handle_message))

    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()

main()

