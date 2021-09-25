import telebot
from telebot import types
from datetime import datetime, date, time
from fuzzywuzzy import process

print("Bot is running")

bot = telebot.TeleBot('')

admin = "0"
ausername = "0"
#admin---------------------------------------------------------------------
@bot.message_handler(commands=['admin'])
def admin_message(message):
    global admin
    sent=bot.send_message(message.from_user.id, "Введи пароль")
    bot.register_next_step_handler(sent, admin_password)

def admin_password(message):
    global admin
    global ausername
    if message.text == "":
        admin=message.from_user.id
        print(admin)
        if bool(message.from_user.username)==True:
            ausername="@"+message.from_user.username
        else:
            ausername='"'+message.from_user.first_name+'"'
        bot.send_message(admin, "Ты теперь админ")
    else:
        bot.send_message(message.from_user.id, "Пароль неверный")
        bot.send_message(message.from_user.id, "Ты не админ")

@bot.message_handler(commands=['adminn'])
def admin_message(message):
    global admin
    global ausername
    if admin=="0":
        bot.send_message(message.from_user.id, "Админ не зарегистрирован")
    else:
        bot.send_message(message.from_user.id, ausername)

@bot.message_handler(commands=['test'])
def admin_message(message):
    bot.send_message(message.from_user.id, "I`m OK")
    
#/admin---------------------------------------------------------------------

@bot.message_handler(commands=['help'])
def help_messaage(message):
    bot.send_message(message.from_user.id, "/start - начать")
    bot.send_message(message.from_user.id, "/review - передать отзыв")
    bot.send_message(message.from_user.id, "/help - помощь")
    bot.send_message(message.from_user.id, "/about - об о мне")

@bot.message_handler(commands=['about'])
def about_messaage(message):
    bot.send_message(message.from_user.id, "Я бот-справочник физики")

@bot.message_handler(commands=['review'])
def review_message(message):
    global admin
    global rusername
    if bool(message.from_user.username)==True:
        rusername="@"+message.from_user.username
    else:
        rusername='"'+message.from_user.first_name+'"'
    sent=bot.send_message(message.from_user.id, "Напиши одним сообщением что ты хочешь что б я передал")
    bot.register_next_step_handler(sent, review_text)

def review_text(message):
    global admin
    global rusername
    bot.send_message(admin, "Новый отзыв от "+rusername+":")
    bot.send_message(admin, message.text)
    bot.send_message(message.from_user.id, "Передал:)")

@bot.message_handler(commands=['start'])
def welcome_message(message):
    user = bot.get_me()
    print("____Time____: "+str(datetime.today()))
    print("____Bot____: "+str(user))
    print("____User____: "+str(message))
    bot.send_message(message.from_user.id, "Привет")
    keyboard = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True, one_time_keyboard=True)
    keyboard.add('Формулы',
                 'Константы',
                 'Десятичные приставки',
                 'Единицы измерения',
                 'Соотношение между различными единицами',
                 'Масса частиц',
                 'Плотность',
                 'Удельная теплоемкость',
                 'Молярные массы',
                 'Плавление элементов',
                 'Удельное сопротивление',
                 'Масса атомов')
    bot.send_message(message.from_user.id, "Какой раздел?", reply_markup=keyboard)

@bot.message_handler(content_types=['text'])
def general_message(message):
    hideBoard = types.ReplyKeyboardRemove()
    #formulas----------------------------------------------------------------------------------------------------
    if message.text.lower() == 'формулы':
        keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=True)
        keyboard.add('Механика',
                     'Законы сохранения в механике',
                     'Колебания и волны',
                     'Молекулярная физика. Тепловые явления',
                     'Гидростатика',
                     'Электродинамика',
                     'Оптика',
                     'Квантовая физика',)
        bot.send_message(message.from_user.id, "Какой раздел?", reply_markup=keyboard)
    elif message.text.lower() == 'механика':
        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
        keyboard.add('Кинематика',
                     'Динамика',
                     'Статика')
        bot.send_message(message.from_user.id, "Какой раздел?", reply_markup=keyboard)
    elif message.text.lower() == 'кинематика':
        bot.send_photo(message.from_user.id, photo=open('photos/Кинематика.png', 'rb'), reply_markup=hideBoard)
    elif message.text.lower() == 'динамика':
        bot.send_photo(message.from_user.id, photo=open('photos/Динамика.png', 'rb'), reply_markup=hideBoard)
    elif message.text.lower() == 'статика':
        bot.send_photo(message.from_user.id, photo=open('photos/Статика.png', 'rb'), reply_markup=hideBoard)
    elif message.text.lower() == 'законы сохранения в механике':
        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
        keyboard.add('Закон сохранения импульса',
                     'Закон сохранения энергии')
        bot.send_message(message.from_user.id, "Какой раздел?", reply_markup=keyboard)
    elif message.text.lower() == 'закон сохранения импульса':
        bot.send_photo(message.from_user.id, photo=open('photos/Закон сохранения импульса.png', 'rb'), reply_markup=hideBoard)
    elif message.text.lower() == 'закон сохранения энергии':
        bot.send_photo(message.from_user.id, photo=open('photos/Закон сохранения энергии1.png', 'rb'), reply_markup=hideBoard)
        bot.send_photo(message.from_user.id, photo=open('photos/Закон сохранения энергии2.png', 'rb'), reply_markup=hideBoard)
    elif message.text.lower() == 'колебания и волны':
        bot.send_photo(message.from_user.id, photo=open('photos/Колебания и волны.png', 'rb'), reply_markup=hideBoard)
    elif message.text.lower() == 'молекулярная физика. тепловые явления':
        bot.send_photo(message.from_user.id, photo=open('photos/Молекулярная физика. Тепловые явления1.png', 'rb'))
        bot.send_photo(message.from_user.id, photo=open('photos/Молекулярная физика. Тепловые явления2.png', 'rb'), reply_markup=hideBoard)
    elif message.text.lower() == 'гидростатика':
        bot.send_photo(message.from_user.id, photo=open('photos/Гидростатика.png', 'rb'))
    elif message.text.lower() == 'электродинамика':
        bot.send_photo(message.from_user.id, photo=open('photos/Электродинамика1.png', 'rb'))
        bot.send_photo(message.from_user.id, photo=open('photos/Электродинамика2.png', 'rb'), reply_markup=hideBoard)
    elif message.text.lower() == 'оптика':
        bot.send_photo(message.from_user.id, photo=open('photos/Оптика.png', 'rb'), reply_markup=hideBoard)
    elif message.text.lower() == 'квантовая физика':
        bot.send_photo(message.from_user.id, photo=open('photos/Квантовая физика.png', 'rb'), reply_markup=hideBoard)
    #other----------------------------------------------------------------------------------------------------
    elif message.text.lower() == 'константы':
        bot.send_photo(message.from_user.id, photo=open('photos/Константы.png', 'rb'), reply_markup=hideBoard)
    elif message.text.lower() == 'десятичные приставки':
        bot.send_photo(message.from_user.id, photo=open('photos/Десятичные приставки.png', 'rb'), reply_markup=hideBoard)
    elif message.text.lower() == 'единицы измерения':
        keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=True)
        keyboard.add('СИ',
                     'Производные от СИ',
                     'Основные',
                     'Время')
        bot.send_message(message.from_user.id, "Какой раздел?", reply_markup=keyboard)
    elif message.text.lower() == 'си':
    	bot.send_photo(message.from_user.id, photo=open('photos/СИ1.png', 'rb'))
    	bot.send_photo(message.from_user.id, photo=open('photos/СИ2.png', 'rb'), reply_markup=hideBoard)
    elif message.text.lower() == 'производные от си':
    	bot.send_photo(message.from_user.id, photo=open('photos/Производные от СИ.png', 'rb'), reply_markup=hideBoard)
    elif message.text.lower() == 'основные':
    	bot.send_photo(message.from_user.id, photo=open('photos/Основные.png', 'rb'), reply_markup=hideBoard)
    elif message.text.lower() == 'время':
    	bot.send_photo(message.from_user.id, photo=open('photos/Время.png', 'rb'), reply_markup=hideBoard)
    elif message.text.lower() == 'соотношение между различными единицами':
        bot.send_photo(message.from_user.id, photo=open('photos/Соотношение между различными единицами.png', 'rb'), reply_markup=hideBoard)
    elif message.text.lower() == 'масса частиц':
        bot.send_photo(message.from_user.id, photo=open('photos/Масса частиц.png', 'rb'), reply_markup=hideBoard)
    elif message.text.lower() == 'плотность':
        bot.send_photo(message.from_user.id, photo=open('photos/Плотность.png', 'rb'), reply_markup=hideBoard)
    elif message.text.lower() == 'удельная теплоемкость':
        bot.send_photo(message.from_user.id, photo=open('photos/Удельная теплоемкость.png', 'rb'), reply_markup=hideBoard)
    elif message.text.lower() == 'молярные массы':
        bot.send_photo(message.from_user.id, photo=open('photos/Молярные массы.png', 'rb'), reply_markup=hideBoard)
    elif message.text.lower() == 'плавление элементов':
        bot.send_photo(message.from_user.id, photo=open('photos/Плавление элементов.png', 'rb'), reply_markup=hideBoard)
    elif message.text.lower() == 'удельное сопротивление':
        bot.send_photo(message.from_user.id, photo=open('photos/Удельное сопротивление.png', 'rb'), reply_markup=hideBoard)
    elif message.text.lower() == 'масса атомов':
        bot.send_photo(message.from_user.id, photo=open('photos/Масса атомов.png', 'rb'), reply_markup=hideBoard)
    else:
        strings = ['Формулы',
                   'Константы',
                   'Десятичные приставки',
                   'Единицы измерения',
                   'Соотношение между различными единицами',
                   'Масса частиц',
                   'Плотность',
                   'Удельная теплоемкость',
                   'Молярные массы',
                   'Плавление элементов',
                   'Удельное сопротивление',
                   'Масса атомов',
                   'Механика',
                   'Законы сохранения в механике',
                   'Колебания и волны',
                   'Молекулярная физика. Тепловые явления',
                   'Электродинамика',
                   'Оптика',
                   'Квантовая физика',
                   'Кинематика',
                   'Динамика',
                   'Статика',
                   'Гидростатика',
                   'Закон сохранения импульса',
                   'Закон сохранения энергии',
                   'Производные от СИ',
                   'СИ',
                   'Основные',
                   'Время']
        res = process.extractOne(message.text.lower(), strings)[0]
        bot.send_message(message.from_user.id, 'Возможно вы имелли ввиду "'+res+'"')
        message.text = res
        general_message(message)




while True:
    try:
        bot.polling(none_stop=True, interval=0)
    except:
        pass