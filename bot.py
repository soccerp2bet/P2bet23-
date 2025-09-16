from telegram.ext import Updater, CommandHandler

# Inserisci qui il tuo token reale
TOKEN = 8208920451:AAGY7Y-xnmgX6w0TTFoSLHcx2B0RMG0GdwI
def start(update, context):
    update.message.reply_text("Ciao! Sono il tuo bot di pronostici ⚽")

def pronostico(update, context):
    update.message.reply_text("Esempio: Over 2.5 con probabilità 65%")

updater = Updater(TOKEN, use_context=True)
dp = updater.dispatcher

dp.add_handler(CommandHandler("start", start))
dp.add_handler(CommandHandler("pronostico", pronostico))

updater.start_polling()
updater.idle()
