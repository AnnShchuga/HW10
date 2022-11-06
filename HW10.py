
import telebot
import datetime
import emoji

def calc_log(msg):
    file = open('calc_log.txt', 'a', encoding='utf-8')
    file.write(f'Дата: {datetime.datetime.now().time()}\n'
               f'ID пользователя: {msg.from_user.id}\n'
               f'Сообщение пользователя: {msg.text}\n')
    file.close()

def calc_log1(msg, answer):
    file = open('calc_log1.log', 'a', encoding='utf-8')
    file.write(f'Дата: {datetime.datetime.now().date()}\n'
               f'Время: {datetime.datetime.now().time()}\n'
               f'ID пользователя: {msg.from_user.id}\n'
               f'Сообщение пользователя: {msg.text}\n'
               f'Сообщение от бота: {answer}\n')
    file.close()

bot = telebot.TeleBot('5503832266:AAHVuUlj6vOR8YbrgEsCrLoceCMeg9BJ2KE')

del_buttons = telebot.types.ReplyKeyboardRemove()

buttons1 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
buttons1.row(telebot.types.KeyboardButton('Комплексные'),
            telebot.types.KeyboardButton('Рациональные'))
buttons1.row(telebot.types.KeyboardButton('Ещё не определился'))

buttons2 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
buttons2.row(telebot.types.InlineKeyboardButton('/'),
            telebot.types.InlineKeyboardButton('*'),
            telebot.types.InlineKeyboardButton('-'),
            telebot.types.InlineKeyboardButton('+'))


@bot.message_handler(commands=['clear'])
def hello(msg: telebot.types.Message):
    try:
        file = open('calc_log1.log', 'w', encoding='utf-8')
        file.close()
        bots_reply = 'Файл с историей был очищен.'
        calc_log1(msg, bots_reply)
        bot.send_message(chat_id=msg.from_user.id,
                         text=f'Лог очищен',
                         reply_markup=del_buttons)
    except Exception:
        bots_reply = 'Произошла ошибка. Ответа от бота не было.'
        calc_log1(msg, bots_reply)


@bot.message_handler(commands=['log'])
def hello(msg: telebot.types.Message):
    try:
        file = open('Calc_log1.log', 'r', encoding='utf-8')
        f = file.read()
        file.close()
        bot.send_message(chat_id=msg.from_user.id,
                         text=f'Лог программы\n{f}',
                         reply_markup=del_buttons)
        bots_reply = 'Бот вывел лог программы'
        calc_log1(msg, bots_reply)
    except Exception:
        bot.send_message(chat_id=msg.from_user.id, parse_mode='HTML',
                         text='<b>Произошла ошибка!</b>\n'
                              'Это может быть связано с большим объёмом информации с файле лога.\n'
                              'Попробуйте очистить лог и повторите запрос.',
                         reply_markup=buttons1)
        bots_reply = 'Произошла ошибка.'
        calc_log1(msg, bots_reply)


@bot.message_handler(commands=['start'])
def hello(msg: telebot.types.Message):
    try:
        bots_reply = 'Бот поприветствовал пользователя и предложил выбор.'
        calc_log1(msg, bots_reply)
        bot.send_message(chat_id=msg.from_user.id, parse_mode='HTML',
                         text=f'<b>Здравствуйте</b> {emoji.emojize(":waving_hand_light_skin_tone:")}\n'
                              'С какими числами будем работать?',
                         reply_markup=buttons1)
        bot.register_next_step_handler(msg, answer)
    except Exception:
        bots_reply = 'Произошла ошибка. Ответа от бота не было.'
        calc_log1(msg, bots_reply)


@bot.message_handler()
def ooops(msg: telebot.types.Message):
    bot.reply_to(msg, "Пожалуйста, выберите одну из команд в меню:\n"
                      "/start - для запуска калькулятора\n"
                      "/calc_log - для вывода истории работы бота\n"
                      "/clear - для очистки истории")
    bots_reply = 'Бот предложил выбрать одну из команд в меню.'
    calc_log1(msg, bots_reply)


@bot.message_handler()
def answer(msg: telebot.types.Message):
    if msg.text == 'Комплексные':
        try:
            bot.register_next_step_handler(msg, complex_counter)
            bot.send_message(chat_id=msg.from_user.id,
                             text='Выберите действие.',
                             reply_markup=buttons2)
            bots_reply = 'Бот предложил выбрать действие.'
            calc_log1(msg, bots_reply)
        except Exception:
            bot.send_message(chat_id=msg.from_user.id,
                             text='Произошла ошибка.',
                             reply_markup=buttons2)
            bots_reply = 'Произошла ошибка.'
            calc_log1(msg, bots_reply)
    elif msg.text == 'Рациональные':
        try:
            bot.register_next_step_handler(msg, rational_counter)
            bot.send_message(chat_id=msg.from_user.id,
                             text='Выберите действие.',
                             reply_markup=buttons2)
            bots_reply = 'Бот предложил выбрать действие.'
            calc_log1(msg, bots_reply)
        except Exception:
            bot.send_message(chat_id=msg.from_user.id,
                             text='Произошла ошибка.',
                             reply_markup=buttons2)
            bots_reply = 'Произошла ошибка.'
            calc_log1(msg, bots_reply)
    elif msg.text == 'Ещё не определился':
        try:
            bot.send_message(chat_id=msg.from_user.id, text='Возвращайтесь, когда определитесь.',
                             reply_markup=del_buttons)
            bots_reply = 'Бот предложил вернуться, когда пользователь определится.'
            calc_log1(msg, bots_reply)
        except Exception:
            bot.send_message(chat_id=msg.from_user.id,
                             text='Произошла ошибка.',
                             reply_markup=buttons2)
            bots_reply = 'Произошла ошибка.'
            calc_log1(msg, bots_reply)
    else:
        try:
            bot.register_next_step_handler(msg, answer)
            bot.send_message(chat_id=msg.from_user.id, text='Пожалуйста, используйте кнопки.')

            bot.send_message(chat_id=msg.from_user.id, text='Выберите режим работы калькулятора.',
                             reply_markup=buttons1)
            bots_reply = 'Пользователь не воспользовался кнопками.'
            calc_log1(msg, bots_reply)
        except Exception:
            bot.send_message(chat_id=msg.from_user.id,
                             text='Произошла ошибка.',
                             reply_markup=buttons2)
            bots_reply = 'Произошла ошибка.'
            calc_log1(msg, bots_reply)


def complex_counter(msg: telebot.types.Message):
    if msg.text == '+':
        try:
            bot.register_next_step_handler(msg, complex_addition)
            bot.send_message(chat_id=msg.from_user.id,
                             text='Введите 4 числа через запятую.',
                             reply_markup=del_buttons)
            bots_reply = 'Бот предложил ввести числа.'
            calc_log1(msg, bots_reply)
        except Exception:
            bot.send_message(chat_id=msg.from_user.id,
                             text='Произошла ошибка.',
                             reply_markup=buttons2)
            bots_reply = 'Произошла ошибка.'
            calc_log1(msg, bots_reply)
    elif msg.text == '-':
        try:
            bot.register_next_step_handler(msg, complex_subtraction)
            bot.send_message(chat_id=msg.from_user.id,
                             text='Введите 4 числа через запятую.',
                             reply_markup=del_buttons)
            bots_reply = 'Бот предложил ввести числа.'
            calc_log1(msg, bots_reply)
        except Exception:
            bot.send_message(chat_id=msg.from_user.id,
                             text='Произошла ошибка.',
                             reply_markup=buttons2)
            bots_reply = 'Произошла ошибка.'
            calc_log1(msg, bots_reply)
    elif msg.text == '*':
        try:
            bot.register_next_step_handler(msg, complex_multiplication)
            bot.send_message(chat_id=msg.from_user.id,
                             text='Введите 4 числа через запятую.',
                             reply_markup=del_buttons)
            bots_reply = 'Бот предложил ввести числа.'
            calc_log1(msg, bots_reply)
        except Exception:
            bot.send_message(chat_id=msg.from_user.id,
                             text='Произошла ошибка.',
                             reply_markup=buttons2)
            bots_reply = 'Произошла ошибка.'
            calc_log1(msg, bots_reply)
    elif msg.text == '/':
        try:
            bot.register_next_step_handler(msg, complex_division)
            bot.send_message(chat_id=msg.from_user.id,
                             text='Введите 4 числа через запятую.',
                             reply_markup=del_buttons)
            bots_reply = 'Бот предложил ввести числа.'
            calc_log1(msg, bots_reply)
        except Exception:
            bot.send_message(chat_id=msg.from_user.id,
                             text='Произошла ошибка.',
                             reply_markup=buttons2)
            bots_reply = 'Произошла ошибка.'
            calc_log1(msg, bots_reply)
    elif msg.text == 'Ещё не определился':
        try:
            bot.send_message(chat_id=msg.from_user.id, text='Возвращайтесь, когда определитесь.',
                             reply_markup=del_buttons)
            bots_reply = 'Бот предложил вернуться, когда пользователь определится.'
            calc_log1(msg, bots_reply)
        except Exception:
            bot.send_message(chat_id=msg.from_user.id,
                             text='Произошла ошибка.',
                             reply_markup=buttons2)
            bots_reply = 'Произошла ошибка.'
            calc_log1(msg, bots_reply)
    else:
        try:
            bot.register_next_step_handler(msg, answer)
            bot.send_message(chat_id=msg.from_user.id, text='Пожалуйста, используйте кнопки.')

            bot.send_message(chat_id=msg.from_user.id, text='С какими числами будем работать?',
                             reply_markup=buttons1)
            bots_reply = 'Пользователь не воспользовался кнопками.'
            calc_log1(msg, bots_reply)
        except Exception:
            bot.send_message(chat_id=msg.from_user.id,
                             text='Произошла ошибка.',
                             reply_markup=buttons2)
            bots_reply = 'Произошла ошибка.'
            calc_log1(msg, bots_reply)


def rational_counter(msg: telebot.types.Message):
    if msg.text == 'Сложение':
        try:
            bot.register_next_step_handler(msg, rational_addition)
            bot.send_message(chat_id=msg.from_user.id,
                             text='Введите несколько чисел через запятую.',
                             reply_markup=del_buttons)
            bots_reply = 'Бот предложил ввести числа.'
            calc_log1(msg, bots_reply)
        except Exception:
            bot.send_message(chat_id=msg.from_user.id,
                             text='Произошла ошибка.',
                             reply_markup=buttons2)
            bots_reply = 'Произошла ошибка.'
            calc_log1(msg, bots_reply)
    elif msg.text == 'Вычитание':
        try:
            bot.register_next_step_handler(msg, rational_subtraction)
            bot.send_message(chat_id=msg.from_user.id,
                             text='Введите несколько чисел через запятую.',
                             reply_markup=del_buttons)
            bots_reply = 'Бот предложил ввести числа.'
            calc_log1(msg, bots_reply)
        except Exception:
            bot.send_message(chat_id=msg.from_user.id,
                             text='Произошла ошибка.',
                             reply_markup=buttons2)
            bots_reply = 'Произошла ошибка.'
            calc_log1(msg, bots_reply)
    elif msg.text == 'Умножение':
        try:
            bot.register_next_step_handler(msg, rational_multiplication)
            bot.send_message(chat_id=msg.from_user.id,
                             text='Введите несколько чисел через запятую.',
                             reply_markup=del_buttons)
            bots_reply = 'Бот предложил ввести числа.'
            calc_log1(msg, bots_reply)
        except Exception:
            bot.send_message(chat_id=msg.from_user.id,
                             text='Произошла ошибка.',
                             reply_markup=buttons2)
            bots_reply = 'Произошла ошибка.'
            calc_log1(msg, bots_reply)
    elif msg.text == 'Деление':
        try:
            bot.register_next_step_handler(msg, rational_division)
            bot.send_message(chat_id=msg.from_user.id,
                             text='Введите несколько чисел через запятую.',
                             reply_markup=del_buttons)
            bots_reply = 'Бот предложил ввести числа.'
            calc_log1(msg, bots_reply)
        except Exception:
            bot.send_message(chat_id=msg.from_user.id,
                             text='Произошла ошибка.',
                             reply_markup=buttons2)
            bots_reply = 'Произошла ошибка.'
            calc_log1(msg, bots_reply)
    elif msg.text == 'Ещё не определился':
        try:
            bot.send_message(chat_id=msg.from_user.id, text='Возвращайтесь, когда определитесь.',
                             reply_markup=del_buttons)
            bots_reply = 'Бот предложил вернуться, когда пользователь определится.'
            calc_log1(msg, bots_reply)
        except Exception:
            bot.send_message(chat_id=msg.from_user.id,
                             text='Произошла ошибка.',
                             reply_markup=buttons2)
            bots_reply = 'Произошла ошибка.'
            calc_log1(msg, bots_reply)
    else:
        try:
            bot.register_next_step_handler(msg, answer)
            bot.send_message(chat_id=msg.from_user.id, text='Пожалуйста, используйте кнопки.')

            bot.send_message(chat_id=msg.from_user.id, text='С какими числами будем работать?',
                             reply_markup=buttons1)
            bots_reply = 'Пользователь не воспользовался кнопками.'
            calc_log1(msg, bots_reply)
        except Exception:
            bot.send_message(chat_id=msg.from_user.id,
                             text='Произошла ошибка.',
                             reply_markup=buttons2)
            bots_reply = 'Произошла ошибка.'
            calc_log1(msg, bots_reply)


def complex_addition(msg: telebot.types.Message):
    try:
        lst = msg.text.split(",")
        new_lst = []
        for i in lst:
            if '.' in i:
                i = float(i)
                new_lst.append(i)
            else:
                i = int(i)
                new_lst.append(i)
        com1 = complex(new_lst[0], new_lst[1])
        com2 = complex(new_lst[2], new_lst[3])
        com_3 = com1 + com2
        res = f'{com1} + {com2} = {com_3}'
        bot.send_message(chat_id=msg.from_user.id,
                         text=f'Ответ: {res}',
                         reply_markup=buttons1)
        bot.register_next_step_handler(msg, answer)
        bot.send_message(chat_id=msg.from_user.id,
                         text='Продолжим?\nС какими числами будем работать?')
        bots_reply = 'Бот предложил продолжить вычисления.'
        calc_log1(msg, bots_reply)
    except Exception:
        bot.register_next_step_handler(msg, complex_addition)
        bot.send_message(chat_id=msg.from_user.id, parse_mode='HTML',
                         text='Что-то пошло не так. Повторите ввод. Введите числа через запятую.\n'
                              '========================================\n'
                              f'{emoji.emojize(":index_pointing_up_light_skin_tone:")}<b>В качестве десятичного '
                              f'разделителя можно использовать только точку</b>',
                         reply_markup=del_buttons)
        bots_reply = 'Произошла ошибка.Бот предложил повторить ввод.'
        calc_log1(msg, bots_reply)


def complex_subtraction(msg: telebot.types.Message):
    try:
        lst = msg.text.split(",")
        new_lst = []
        for i in lst:
            if '.' in i:
                i = float(i)
                new_lst.append(i)
            else:
                i = int(i)
                new_lst.append(i)
        com1 = complex(new_lst[0], new_lst[1])
        com2 = complex(new_lst[2], new_lst[3])
        com_3 = com1 - com2
        res = f'{com1} - {com2} = {com_3}'
        bot.send_message(chat_id=msg.from_user.id,
                         text=f'Ответ: {res}',
                         reply_markup=buttons1)
        bot.register_next_step_handler(msg, answer)
        bot.send_message(chat_id=msg.from_user.id,
                         text='Продолжим?\nС какими числами будем работать?')
        bots_reply = 'Бот предложил продолжить вычисления.'
        calc_log1(msg, bots_reply)
    except Exception:
        bot.register_next_step_handler(msg, complex_subtraction)
        bot.send_message(chat_id=msg.from_user.id, parse_mode='HTML',
                         text='Что-то пошло не так. Повторите ввод.\nВведите числа через запятую.\n'
                              f'{emoji.emojize(":index_pointing_up_light_skin_tone:")}<b>В качестве десятичного '
                              f'разделителя можно использовать только точку</b>',
                         reply_markup=del_buttons)
        bots_reply = 'Произошла ошибка.Бот предложил повторить ввод.'
        calc_log1(msg, bots_reply)


def complex_multiplication(msg: telebot.types.Message):
    try:
        lst = msg.text.split(",")
        new_lst = []
        for i in lst:
            if '.' in i:
                i = float(i)
                new_lst.append(i)
            else:
                i = int(i)
                new_lst.append(i)
        com1 = complex(new_lst[0], new_lst[1])
        com2 = complex(new_lst[2], new_lst[3])
        com_3 = com1 * com2
        res = f'{com1} * {com2} = {com_3}'
        bot.send_message(chat_id=msg.from_user.id,
                         text=f'Ответ: {res}',
                         reply_markup=buttons1)
        bot.register_next_step_handler(msg, answer)
        bot.send_message(chat_id=msg.from_user.id,
                         text='Продолжим?\nС какими числами будем работать?')
        bots_reply = 'Бот предложил продолжить вычисления.'
        calc_log1(msg, bots_reply)
    except Exception:
        bot.register_next_step_handler(msg, complex_multiplication)
        bot.send_message(chat_id=msg.from_user.id, parse_mode='HTML',
                         text='Что-то пошло не так. Повторите ввод. Введите числа через запятую.\n'
                              f'{emoji.emojize(":index_pointing_up_light_skin_tone:")}'
                              '<b>В качестве десятичного разделителя можно использовать только точку</b>',
                         reply_markup=del_buttons)
        bots_reply = 'Произошла ошибка.Бот предложил повторить ввод.'
        calc_log1(msg, bots_reply)


def complex_division(msg: telebot.types.Message):
    try:
        lst = msg.text.split(",")
        new_lst = []
        for i in lst:
            if '.' in i:
                i = float(i)
                new_lst.append(i)
            else:
                i = int(i)
                new_lst.append(i)
        com1 = complex(new_lst[0], new_lst[1])
        com2 = complex(new_lst[2], new_lst[3])
        com_3 = com1 / com2
        res = f'{com1} / {com2} = {com_3}'
        bot.send_message(chat_id=msg.from_user.id,
                         text=f'Ответ: {res}',
                         reply_markup=buttons1)
        bot.register_next_step_handler(msg, answer)
        bot.send_message(chat_id=msg.from_user.id,
                         text='Продолжим?\n'
                              'С какими числами будем работать?')
        bots_reply = 'Бот предложил продолжить вычисления.'
        calc_log1(msg, bots_reply)
    except Exception:
        bot.register_next_step_handler(msg, complex_division)
        bot.send_message(chat_id=msg.from_user.id, parse_mode='HTML',
                         text='Что-то пошло не так. Повторите ввод. Введите числа через запятую. '
                              'В качестве десятичного разделителя можно использовать только точку.\n'
                              '\n'
                              '=============================\n'
                              f'{emoji.emojize(":index_pointing_up_light_skin_tone:")}<b>На 0 делить нельзя!\n'
                              'Оба последних числа не должны быть отрицательными</b>',
                         reply_markup=del_buttons)
        bots_reply = 'Произошла ошибка.Бот предложил повторить ввод.'
        calc_log1(msg, bots_reply)


def rational_addition(msg: telebot.types.Message):
    try:
        lst = msg.text.split(",")
        new_lst = []
        for i in lst:
            if '.' in i:
                i = float(i)
                new_lst.append(i)
            else:
                i = int(i)
                new_lst.append(i)
        lst_1 = []
        for item in new_lst[1:]:
            if item < 0:
                lst_1.append(str(item))
                string = ''.join(lst_1)
                lst_2 = [int(i) for i in lst_1]
                res = f'{new_lst[0]}{string} = {new_lst[0] + sum(lst_2)}'
            else:
                string = ' + '.join(lst)
                res = f'{string} = {new_lst[0] + sum(new_lst[1:])}'
            bot.send_message(chat_id=msg.from_user.id,
                         text=f'Ответ: {res}',
                         reply_markup=buttons1)
        bot.register_next_step_handler(msg, answer)
        bot.send_message(chat_id=msg.from_user.id,
                         text='Продолжим?\nС какими числами будем работать?')
        bots_reply = 'Бот предложил продолжить вычисления.'
        calc_log1(msg, bots_reply)
    except Exception:
        bot.register_next_step_handler(msg, rational_addition)
        bot.send_message(chat_id=msg.from_user.id, parse_mode='HTML',
                         text='Что-то пошло не так. Повторите ввод. Введите числа через запятую. '
                              f'{emoji.emojize(":index_pointing_up_light_skin_tone:")}'
                              '<b>В качестве десятичного разделителя можно использовать только точку</b>',
                         reply_markup=del_buttons)
        bots_reply = 'Произошла ошибка.Бот предложил повторить ввод.'
        calc_log1(msg, bots_reply)


def rational_subtraction(msg: telebot.types.Message):
    try:
        lst = msg.text.split(",")
        new_lst = []
        for i in lst:
            if '.' in i:
                i = float(i)
                new_lst.append(i)
            else:
                i = int(i)
                new_lst.append(i)
        lst_1 = []
        for item in new_lst[1:]:
            if item < 0:
                item *= -1
                lst_1.append(str(item))
                string = ' + '.join(lst_1)
                lst_2 = [int(i) for i in lst_1]
                res = f'{new_lst[0]} + {string} = {new_lst[0] + sum(lst_2)}'
            else:
                string = ' - '.join(lst)
                res = f'{string} = {new_lst[0] - sum(new_lst[1:])}'
            bot.send_message(chat_id=msg.from_user.id,
                         text=f'Ответ: {res}',
                         reply_markup=buttons1)
        bot.register_next_step_handler(msg, answer)
        bot.send_message(chat_id=msg.from_user.id,
                         text='Продолжим?\n'
                              'С какими числами будем работать?')
        bots_reply = 'Бот предложил продолжить вычисления.'
        calc_log1(msg, bots_reply)
    except Exception:
        bot.register_next_step_handler(msg, rational_subtraction)
        bot.send_message(chat_id=msg.from_user.id, parse_mode='HTML',
                         text='Что-то пошло не так. Повторите ввод. Введите числа через запятую. '
                              f'{emoji.emojize(":index_pointing_up_light_skin_tone:")}'
                              '<b>В качестве десятичного разделителя можно использовать только точку</b>',
                         reply_markup=del_buttons)
        bots_reply = 'Произошла ошибка.Бот предложил повторить ввод.'
        calc_log1(msg, bots_reply)


def rational_multiplication(msg: telebot.types.Message):
    try:
        lst = msg.text.split(",")
        new_lst = []
        for i in lst:
            if '.' in i:
                i = float(i)
                new_lst.append(i)
            else:
                i = int(i)
                new_lst.append(i)
        p = 1
        for i in new_lst:
            p *= i
        string = ' * '.join(lst)
        res = f'{string} = {p}'
        bot.send_message(chat_id=msg.from_user.id,
                         text=f'Ответ: {res}',
                         reply_markup=buttons1)
        bot.register_next_step_handler(msg, answer)
        bot.send_message(chat_id=msg.from_user.id,
                         text='Продолжим?\n'
                              'С какими числами будем работать?')
        bots_reply = 'Бот предложил продолжить вычисления.'
        calc_log1(msg, bots_reply)
    except Exception:
        bot.register_next_step_handler(msg, rational_multiplication)
        bot.send_message(chat_id=msg.from_user.id, parse_mode='HTML',
                         text='Что-то пошло не так. Повторите ввод. Введите числа через запятую. '
                              f'{emoji.emojize(":index_pointing_up_light_skin_tone:")}'
                              '<b>В качестве десятичного разделителя можно использовать только точку</b>',
                         reply_markup=del_buttons)
        bots_reply = 'Произошла ошибка.Бот предложил повторить ввод.'
        calc_log1(msg, bots_reply)


def rational_division(msg: telebot.types.Message):
    try:
        lst = msg.text.split(",")
        new_lst = []
        for i in lst:
            if '.' in i:
                i = float(i)
                new_lst.append(i)
            else:
                i = int(i)
                new_lst.append(i)
        p = 1
        for i in new_lst:
            p /= i
        string = ' / '.join(lst)
        res = f'{string} = {p}'
        bot.send_message(chat_id=msg.from_user.id,
                         text=f'Ответ: {res}',
                         reply_markup=buttons1)
        bot.register_next_step_handler(msg, answer)
        bot.send_message(chat_id=msg.from_user.id,
                         text='Продолжим?\n'
                              'С какими числами будем работать?')
        bots_reply = 'Бот предложил продолжить вычисления.'
        calc_log1(msg, bots_reply)
    except Exception:
        bot.register_next_step_handler(msg, rational_division)
        bot.send_message(chat_id=msg.from_user.id, parse_mode='HTML',
                         text='Что-то пошло не так. Повторите ввод. Введите числа через запятую. '
                              '<b>В качестве десятичного разделителя можно использовать только точку</b>\n'
                              '\n'
                              '=============================\n'
                              f'{emoji.emojize(":index_pointing_up_light_skin_tone:")}'
                              '<b>На 0 делить нельзя!</b>',
                         reply_markup=del_buttons)
        bots_reply = 'Произошла ошибка.Бот предложил повторить ввод.'
        calc_log1(msg, bots_reply)
        

bot.polling(non_stop=True)
