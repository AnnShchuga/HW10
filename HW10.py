
import telebot

bot = telebot.TeleBot('5503832266:AAHVuUlj6vOR8YbrgEsCrLoceCMeg9BJ2KE')

buttons = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
buttons.row(telebot.types.KeyboardButton('Комплексные'),
            telebot.types.KeyboardButton('Рациональные'),
            telebot.types.KeyboardButton('Ещё не определился'))


@bot.message_handler()
def hello(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id,
                     text='Здравствуйте.\nВыберите режим работы калькулятора.',
                     reply_markup=buttons)
    bot.register_next_step_handler(msg, answer)


def answer(msg: telebot.types.Message):
    if msg.text == 'Комплексные':
        bot.register_next_step_handler(msg, complex_counter)
        bot.send_message(chat_id=msg.from_user.id,
                         text='Введите выражение с комплексными числами.',
                         reply_markup=telebot.types.ReplyKeyboardRemove())
    elif msg.text == 'Рациональные':
        bot.register_next_step_handler(msg, rational_counter)
        bot.send_message(chat_id=msg.from_user.id,
                         text='Введите выражение с рациональными числами.',
                         reply_markup=telebot.types.ReplyKeyboardRemove())
    elif msg.text == 'Ещё не определился':
        bot.register_next_step_handler(msg, answer)
        bot.send_message(chat_id=msg.from_user.id, text='Возвращайтесь, когда определитесь.')
    else:
        bot.register_next_step_handler(msg, answer)
        bot.send_message(chat_id=msg.from_user.id, text='Пожалуйста, используйте кнопки.')

        bot.send_message(chat_id=msg.from_user.id, text='Выберите режим работы калькулятора.', reply_markup=buttons)


def complex_counter(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id, text=msg.text.upper(), reply_markup=telebot.types.ReplyKeyboardRemove())


def rational_counter(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id, text=msg.text.lower(), reply_markup=telebot.types.ReplyKeyboardRemove()

                                                                                   @ bot.message_handler()

    bot.polling()