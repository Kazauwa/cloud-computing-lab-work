import logging

import config
from models import ValueList, session
from telegram import ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, \
    ConversationHandler, RegexHandler


def start(bot, update):
    reply_keyboard = [
        ['Show all values'],
        ['Add value'],
        ['Remove value']
    ]
    reply_markup = ReplyKeyboardMarkup(
        reply_keyboard, one_time_keyboard=True, resize_keyboard=True
    )
    update.message.reply_text('Choose one of the options below. '
                              'You can use /start anytime to cancel adding '
                              'or removing value and return here.',
                              reply_markup=reply_markup)
    return 'MAIN_MENU'


def show_all_values_handler(bot, update):
    values = session.query(ValueList).all()
    if values:
        enumerated_list = ['{}. {}'.format(index, element.value)
                           for index, element in enumerate(values, start=1)]
        formatted_todo_list = '\n'.join(enumerated_list)
        update.message.reply_text(formatted_todo_list)
    else:
        update.message.reply_text('List is empty!')
    return start(bot, update)


def add_value_instruction_handler(bot, update):
    update.message.reply_text('Input the desired value')
    return 'ADD_VALUE'


def remove_value_instruction_handler(bot, update):
    update.message.reply_text('Specify index for value to drop')
    return 'REMOVE_VALUE'


def add_value_handler(bot, update):
    new_value = ValueList(value=update.message.text)
    session.add(new_value)
    session.commit()
    return start(bot, update)


def remove_value_handler(bot, update):
    all_values = session.query(ValueList).all()
    user_input = update.message.text
    if not user_input.isdigit():
        update.message.reply_text('Index must be integer!')
        return
    todo_list_index = int(user_input)
    if todo_list_index > len(all_values) or todo_list_index <= 0:
        update.message.reply_text('No such index!')
        return
    value_to_remove = all_values[todo_list_index - 1]
    session.delete(value_to_remove)
    session.commit()
    return start(bot, update)


def main():
    updater = Updater(config.TELEGRAM_TOKEN)

    dp = updater.dispatcher

    converstaion = {
        'MAIN_MENU': [
            RegexHandler('^Show all values$', show_all_values_handler),
            RegexHandler('^Add value$', add_value_instruction_handler),
            RegexHandler('^Remove value$', remove_value_instruction_handler)
        ],
        'ADD_VALUE': [MessageHandler(Filters.text, add_value_handler)],

        'REMOVE_VALUE': [MessageHandler(Filters.text, remove_value_handler)],
    }

    dp.add_handler(ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states=converstaion,
        fallbacks=[CommandHandler('start', start)]
    ))

    logging.basicConfig(level=logging.DEBUG)
    logging.getLogger(__name__)

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
