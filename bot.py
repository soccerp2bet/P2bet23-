from telegram.ext import Updater, CommandHandler

TOKEN = "IL_TUO_TOKEN"

def start(update, context):
    update.message.reply_text("Ciao! Bot online 24/7 ✅")

updater = Updater(TOKEN)
dp = updater.dispatcher
dp.add_handler(CommandHandler("start", start))

updater.start_polling()
updater.idle()
