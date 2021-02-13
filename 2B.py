import telebot
from telebot import types


bot = telebot.TeleBot("1651837074:AAHApgwaQJFHtC2Zc4c9ekwQpaToOT4x4do")

keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard1.row('Регистрация')

iin = ''
oin = ''
company = ''


@bot.message_handler(commands=['start'])
def send_text(message):
    bot.send_message(message.chat.id, "Зарегистрируйтесь", reply_markup=keyboard1)


@bot.message_handler(content_types=['text'])
def start(message):
    if message.text.lower() == 'регистрация':
        bot.send_message(message.from_user.id, 'Введите ИИН')
        bot.register_next_step_handler(message, get_iin)


def get_iin(message):
    global iin
    iin = message.text
    bot.send_message(message.from_user.id, 'Введите БИН')
    bot.register_next_step_handler(message, get_oin)


def get_oin(message):
    global oin
    oin = message.text
    bot.send_message(message.from_user.id, 'Введите название компании')
    bot.register_next_step_handler(message, get_company)


def get_company(message):
    global company
    company = message.text
    keyboard = types.InlineKeyboardMarkup()
    key_yes = types.InlineKeyboardButton(text='Да', callback_data='yes')
    keyboard.add(key_yes)  # добавляем кнопку в клавиатуру
    key_no = types.InlineKeyboardButton(text='Нет', callback_data='no')
    keyboard.add(key_no)
    question = 'Ваш ИИН: ' + iin + '\nВаш БИН ' + oin + '\nНазвание компании - ' + company + '?'
    bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "yes":
        bot.send_message(call.message.chat.id, 'Четко, отправьте стикер)')
    elif call.data == "no":
        bot.send_message(call.message.chat.id, 'Пройдите регистрацию сначала', reply_markup=keyboard1)


@bot.message_handler(content_types=['sticker'])
def send_text(message):
    bot.send_message(message.chat.id, "А если скажут с моста прыгни?")


bot.polling()
