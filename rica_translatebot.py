
# -*- coding: utf-8 -*-

import logging
from random import randrange
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters, ConversationHandler)
# from googletrans import Translator
from google_trans_new import google_translator  


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

logger = logging.getLogger(__name__)


translator = google_translator()  





def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text='''translator bot started. type /help for help.''')
    return


def help(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text='''
/t [SOURCE] [TARGET] [MESSAGE]
        translates a message from source language to target language.
        [SOURCE]: source language coded in 2 characters: EN - english, ES - spanish, TR - turkish, FR - french...
        [TARGET]: target language coded in 2 characters: EN - english, ES - spanish, TR - turkish, FR - french...
        [MESSAGE]: message in SOURCE language to be translated to TARGET language.
\n/tr MESSAGE
        translates a message from english to turkish.
        [MESSAGE]: message in turkish to be translated to english.
\n/en MESSAGE
        translates a message from turkish to english.
        [MESSAGE]: message in english to be translated to turkish.
                             ''')
    return

def t(update, context):

    logger.info("%s", update.message.text)
    dst = context.args[1]
    src = context.args[0]
    input=""
    for i in range(2, len(context.args)):
        input += context.args[i] + " "
    print(src)
    print(dst)
    print(input)

    output = translator.translate(input,lang_src=src, lang_tgt=dst)  
    print(output)

    context.bot.send_message(chat_id=update.effective_chat.id, text=output)
    return



def tr(update, context):

    logger.info("%s", update.message.text)
    dest = "tr"

    input=""
    for i in range(0, len(context.args)):
        input += context.args[i] + " "
    
    print(dest)
    print(input)

    output = translator.translate(input,lang_tgt=dest)  
    print(output)

    context.bot.send_message(chat_id=update.effective_chat.id, text=output)
    return



def en(update, context):

    logger.info("%s", update.message.text)
    dest = "en"

    input=""
    for i in range(0, len(context.args)):
        input += context.args[i] + " "
    
    print(dest)
    print(input)

    output = translator.translate(input,lang_tgt=dest)  
    print(output)

    context.bot.send_message(chat_id=update.effective_chat.id, text=output)
    return




def error(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text='what? what is ' + update.message.text + ' 😣😖🤯?????')


def main():


    token = open('TOKEN', 'r').readline()
    updater = Updater(token, use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('help', help))

    dp.add_handler(CommandHandler('t', t, pass_args=True))

    dp.add_handler(CommandHandler('tr', tr, pass_args=True))
    dp.add_handler(CommandHandler('en', en, pass_args=True))


    dp.add_handler(MessageHandler(Filters.regex('^(/[a-zA-Z]+)'), error))

    dp.add_error_handler(error)

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
