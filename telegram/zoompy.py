
import logging

from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)



def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Hola!')
    update.message.reply_text('Soy ZoomPy')
    update.message.reply_text('Puedes utilizarme para generar salas de zoom en segundos')

def help_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('En que puedo ayudarte?')

def echo(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Escribiste : "+update.message.text)


def main():
    updater = Updater("1616811167:AAEwTEycFqEvy8O9fLoI3C9Zs12tb6qmc7A")
    dispatcher = updater.dispatcher

    # commands
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))

    # non-commands
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Start the Bot
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
