
# -*- coding: utf-8 -*-

import logging
from random import randrange
from telegram.ext import (Updater, CommandHandler,
                          MessageHandler, Filters, ConversationHandler)

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

logger = logging.getLogger(__name__)


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text='''ready to roll!\n
                             use the command **</roll NdD>** where N is the amount of dice you want to roll and D the amount of faces the die will have.
                             ''')
    return


def roll(update, context):

    logger.info("%s", update.message.text)
    s = context.args[0]
    N = int(s[0:s.find('d')])
    D = int(s[s.find('d')+1:])

    rolls = []
    total = 0
    for i in range(N):
        pass
        rolls.append(randrange(1, D+1))
        total += rolls[i]

    context.bot.send_message(chat_id=update.effective_chat.id,
                             text='rolling ' + context.args[0] + '\nrolls: ' + str(rolls) + '\ntotal: ' + str(total))
    return


def error(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():

    token = open('TOKEN', 'r').readline()
    updater = Updater(token, use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('roll', roll, pass_args=True))

    dp.add_error_handler(error)

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
