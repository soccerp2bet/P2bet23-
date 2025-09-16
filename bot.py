import os
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

TOKEN = os.getenv("BOT_TOKEN")  # prende il token dalle Config Vars

def start(update: Update, context: CallbackContext):
    update.message.reply_text("Ciao! Il bot è attivo su Heroku 🚀")

updater = Updater(TOKEN)
updater.dispatcher.add_handler(CommandHandler("start", start))

updater.start_polling()
updater.idle()
