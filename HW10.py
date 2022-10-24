
import telebot

bot = telebot.TeleBot('5503832266:AAHVuUlj6vOR8YbrgEsCrLoceCMeg9BJ2KE')

del_buttons=telebot.types.ReplyKeyboardRemove())

buttons1 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
buttons1.row(telebot.types.KeyboardButton('Комплексные'),
            telebot.types.KeyboardButton('Рациональные'))
buttons1.row(telebot.types.KeyboardButton('Ещё не определился'),
            telebot.types.KeyboardButton('Выход'))

buttons2 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
buttons2.row(telebot.types.InlineKeybeardButton('/'),
            telebot.types.InlineKeybeardButton('*'),
            telebot.types.InlineKeybeardButton('-'),
            telebot.types.InlineKeybeardButton('+'),
            telebot.types.InlineKeybeardButton('Выход'))


@ bot.message_handler(commands=['log'])
def hello(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id,
                     text='Лог программы\nИстория вычислений',
                     reply_markup=del_buttons)
    bot.send_message(chat_id=msg.from_user.id, document=open('Calc_log', 'rb')


@ bot.message_handler(commands=['document'])
    def hello(msg: telebot.types.Message):
        file = bot.get_file(msg.document.file_id)
        downloaded_file = bot.download_file(file.file_path)
        with open(msg.document.file_name. 'wb') as f_out:
            f_out.write(downloaded_file)



@bot.message_handler()
def hello(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id,
                     text='Здравствуйте.\nВыберите режим работы калькулятора.',
                     reply_markup=buttons1)
    bot.register_next_step_handler(msg, answer)


def answer(msg: telebot.types.Message):
    if msg.text == 'Комплексные':
        bot.register_next_step_handler(msg, first_step_complex_counter)
        bot.send_message(chat_id=msg.from_user.id,
                         text='Введите выражение с комплексными числами.',
                         reply_markup=del_buttons1)
    elif msg.text == 'Рациональные':
        bot.register_next_step_handler(msg, first_step_rational_counter)
        bot.send_message(chat_id=msg.from_user.id,
                         text='Введите число',
                         reply_markup=del_buttons))
    elif msg.text == 'Ещё не определился':
        bot.register_next_step_handler(msg, answer)
        bot.send_message(chat_id=msg.from_user.id, text='Возвращайтесь, когда определитесь.')
    else:
        bot.register_next_step_handler(msg, answer)
        bot.send_message(chat_id=msg.from_user.id, text='Пожалуйста, используйте кнопки.')

        bot.send_message(chat_id=msg.from_user.id, text='Выберите режим работы калькулятора.', reply_markup=buttons1)




    def first_step_rational_counter(msg: telebot.types.Message):
        if msg.text.isdigit():
            bot.register_next_step_handler(msg, second_step_rational_counter)
            bot.send_message(chat_id=msg.from_user.id,
                            text='Введите второе число.',
                            reply_markup=del_buttons)
        else:
            bot.register_next_step_handler(msg, second_step_rational_counter)
            bot.send_message(chat_id=msg.from_user.id,
                             text='Проверьте правильность написания первого числа.',
                             reply_markup=del_buttons)


    def second_step_rational_counter(msg: telebot.types.Message):
        if msg.text.isdigit():
            bot.register_next_step_handler(msg, third_step_rational_counter)
            bot.send_message(chat_id=msg.from_user.id,
                         text='Введите выражение',
                         reply_markup=buttons2)
        else:
            bot.register_next_step_handler(msg, second_step_rational_counter)
            bot.send_message(chat_id=msg.from_user.id,
                             text='Проверьте правильность написания второго числа.',
                             reply_markup=del_button)


    def third_step_rational_counter(msg: telebot.types.Message):
        if msg.text in {"+", "-", "*", "/"}:
            if msg.text == "+":
                pass
        else:
            bot.send_message(chat_id=msg.from_user.id,
                             text='Используйте кнопки!',
                             reply_markup=buttons2)





    def first_step_complex_counter(msg: telebot.types.Message):
        if msg.text.isdigit():
            bot.register_next_step_handler(msg, second_step_complex_counter)
            bot.send_message(chat_id=msg.from_user.id,
                             text='Введите второе число.',
                             reply_markup=del_buttons)
        else:
            bot.register_next_step_handler(msg, second_step_complex_counter)
            bot.send_message(chat_id=msg.from_user.id,
                             text='Проверьте правильность написания первого числа.',
                             reply_markup=del_buttons)

    def second_step_complex_counter(msg: telebot.types.Message):
        if msg.text.isdigit():
            bot.register_next_step_handler(msg, third_step_complex_counter)
            bot.send_message(chat_id=msg.from_user.id,
                             text='Введите выражение',
                             reply_markup=buttons2)
        else:
            bot.register_next_step_handler(msg, second_step_complex_counter)
            bot.send_message(chat_id=msg.from_user.id,
                             text='Проверьте правильность написания второго числа.',
                             reply_markup=del_button)

    def third_step_complex_counter(msg: telebot.types.Message):
        if msg.text in {"+", "-", "*", "/"}:
            if msg.text == "+":
                pass
        else:
            bot.send_message(chat_id=msg.from_user.id,
                             text='Используйте кнопки!',
                             reply_markup=buttons2)

    bot.polling()
