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
    bot.send_message(message.from_user.id, "Я бот-справочник")

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
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
    keyboard.add('Физика',
                 'Математика')
    bot.send_message(message.from_user.id, "Какой предмет?", reply_markup=keyboard)

@bot.message_handler(content_types=['text'])
def general_message(message):
    hideBoard = types.ReplyKeyboardRemove()
    #phys--------------------------------------------------------------------------------------------------------
    if message.text.lower() == 'физика':
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
    #formulas----------------------------------------------------------------------------------------------------
    elif message.text.lower() == 'формулы':
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
        bot.send_photo(message.from_user.id, photo=open('photos/Физика/Кинематика.png', 'rb'), reply_markup=hideBoard)
    elif message.text.lower() == 'динамика':
        bot.send_photo(message.from_user.id, photo=open('photos/Физика/Динамика.png', 'rb'), reply_markup=hideBoard)
    elif message.text.lower() == 'статика':
        bot.send_photo(message.from_user.id, photo=open('photos/Физика/Статика.png', 'rb'), reply_markup=hideBoard)
    elif message.text.lower() == 'законы сохранения в механике':
        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
        keyboard.add('Закон сохранения импульса',
                     'Закон сохранения энергии')
        bot.send_message(message.from_user.id, "Какой раздел?", reply_markup=keyboard)
    elif message.text.lower() == 'закон сохранения импульса':
        bot.send_photo(message.from_user.id, photo=open('photos/Физика/Закон сохранения импульса.png', 'rb'), reply_markup=hideBoard)
    elif message.text.lower() == 'закон сохранения энергии':
        bot.send_photo(message.from_user.id, photo=open('photos/Физика/Закон сохранения энергии1.png', 'rb'), reply_markup=hideBoard)
        bot.send_photo(message.from_user.id, photo=open('photos/Физика/Закон сохранения энергии2.png', 'rb'), reply_markup=hideBoard)
    elif message.text.lower() == 'колебания и волны':
        bot.send_photo(message.from_user.id, photo=open('photos/Физика/Колебания и волны.png', 'rb'), reply_markup=hideBoard)
    elif message.text.lower() == 'молекулярная физика. тепловые явления':
        bot.send_photo(message.from_user.id, photo=open('photos/Физика/Молекулярная физика. Тепловые явления1.png', 'rb'))
        bot.send_photo(message.from_user.id, photo=open('photos/Физика/Молекулярная физика. Тепловые явления2.png', 'rb'), reply_markup=hideBoard)
    elif message.text.lower() == 'гидростатика':
        bot.send_photo(message.from_user.id, photo=open('photos/Физика/Гидростатика.png', 'rb'))
    elif message.text.lower() == 'электродинамика':
        bot.send_photo(message.from_user.id, photo=open('photos/Физика/Электродинамика1.png', 'rb'))
        bot.send_photo(message.from_user.id, photo=open('photos/Физика/Электродинамика2.png', 'rb'), reply_markup=hideBoard)
    elif message.text.lower() == 'оптика':
        bot.send_photo(message.from_user.id, photo=open('photos/Физика/Оптика.png', 'rb'), reply_markup=hideBoard)
    elif message.text.lower() == 'квантовая физика':
        bot.send_photo(message.from_user.id, photo=open('photos/Физика/Квантовая физика.png', 'rb'), reply_markup=hideBoard)
    #other----------------------------------------------------------------------------------------------------
    elif message.text.lower() == 'константы':
        bot.send_photo(message.from_user.id, photo=open('photos/Физика/Константы.png', 'rb'), reply_markup=hideBoard)
    elif message.text.lower() == 'десятичные приставки':
        bot.send_photo(message.from_user.id, photo=open('photos/Физика/Десятичные приставки.png', 'rb'), reply_markup=hideBoard)
    elif message.text.lower() == 'единицы измерения':
        keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=True)
        keyboard.add('СИ',
                     'Производные от СИ',
                     'Основные',
                     'Время')
        bot.send_message(message.from_user.id, "Какой раздел?", reply_markup=keyboard)
    elif message.text.lower() == 'си':
    	bot.send_photo(message.from_user.id, photo=open('photos/Физика/СИ1.png', 'rb'))
        bot.send_photo(message.from_user.id, photo=open('photos/Физика/СИ2.png', 'rb'), reply_markup=hideBoard)
    elif message.text.lower() == 'производные от си':
    	bot.send_photo(message.from_user.id, photo=open('photos/Физика/Производные от СИ.png', 'rb'), reply_markup=hideBoard)
    elif message.text.lower() == 'основные':
    	bot.send_photo(message.from_user.id, photo=open('photos/Физика/Основные.png', 'rb'), reply_markup=hideBoard)
    elif message.text.lower() == 'время':
    	bot.send_photo(message.from_user.id, photo=open('photos/Физика/Время.png', 'rb'), reply_markup=hideBoard)
    elif message.text.lower() == 'соотношение между различными единицами':
        bot.send_photo(message.from_user.id, photo=open('photos/Физика/Соотношение между различными единицами.png', 'rb'), reply_markup=hideBoard)
    elif message.text.lower() == 'масса частиц':
        bot.send_photo(message.from_user.id, photo=open('photos/Физика/Масса частиц.png', 'rb'), reply_markup=hideBoard)
    elif message.text.lower() == 'плотность':
        bot.send_photo(message.from_user.id, photo=open('photos/Физика/Плотность.png', 'rb'), reply_markup=hideBoard)
    elif message.text.lower() == 'удельная теплоемкость':
        bot.send_photo(message.from_user.id, photo=open('photos/Физика/Удельная теплоемкость.png', 'rb'), reply_markup=hideBoard)
    elif message.text.lower() == 'молярные массы':
        bot.send_photo(message.from_user.id, photo=open('photos/Физика/Молярные массы.png', 'rb'), reply_markup=hideBoard)
    elif message.text.lower() == 'плавление элементов':
        bot.send_photo(message.from_user.id, photo=open('photos/Физика/Плавление элементов.png', 'rb'), reply_markup=hideBoard)
    elif message.text.lower() == 'удельное сопротивление':
        bot.send_photo(message.from_user.id, photo=open('photos/Физика/Удельное сопротивление.png', 'rb'), reply_markup=hideBoard)
    elif message.text.lower() == 'масса атомов':
        bot.send_photo(message.from_user.id, photo=open('photos/Физика/Масса атомов.png', 'rb'), reply_markup=hideBoard)
    #math--------------------------------------------------------------------------------------------------------
    elif message.text.lower() == 'математика':
        keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=True)
        keyboard.add('Алгебра',
                     'Геометрия',
                     'Тригонометрия',
                     'Таблицы')
        bot.send_message(message.from_user.id, "Какой раздел?", reply_markup=keyboard)
    elif message.text.lower() == 'алгебра':
        keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=True)
        keyboard.add('Формулы сокращенного умножения',
                     'Парабола',
                     'Свойства степеней и корней',
                     'Лагорифмы',
                     'Арифметическая прогрессия',
                     'Геометрическая прогрессия',
                     'Квадратные уравнения')
        bot.send_message(message.from_user.id, "Какой раздел?", reply_markup=keyboard)
    elif message.text.lower() == 'формулы сокращенного умножения':
        bot.send_photo(message.from_user.id, photo=open('photos/Математика/Формулы сокращенного умножения.png', 'rb'), reply_markup=hideBoard)
    elif message.text.lower() == 'парабола':
        bot.send_photo(message.from_user.id, photo=open('photos/Математика/Парабола.png', 'rb'), reply_markup=hideBoard)
    elif message.text.lower() == 'свойства степеней и корней':
        bot.send_photo(message.from_user.id, photo=open('photos/Математика/Свойства степеней и корней.png', 'rb'), reply_markup=hideBoard)
    elif message.text.lower() == 'лагорифмы':
        bot.send_photo(message.from_user.id, photo=open('photos/Математика/Лагорифмы.png', 'rb'), reply_markup=hideBoard)
    elif message.text.lower() == 'арифметическая прогрессия':
        bot.send_photo(message.from_user.id, photo=open('photos/Математика/Арифметическая прогрессия.png', 'rb'), reply_markup=hideBoard)
    elif message.text.lower() == 'геометрическая прогрессия':
        bot.send_photo(message.from_user.id, photo=open('photos/Математика/Геометрическая прогрессия.png', 'rb'), reply_markup=hideBoard)
    elif message.text.lower() == 'квадратные уравнения':
        bot.send_photo(message.from_user.id, photo=open('photos/Математика/Квадратные уравнения.png', 'rb'), reply_markup=hideBoard)
    elif message.text.lower() == 'геометрия':
        keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=True)
        keyboard.add('Геометрия треугольников',
                     'Геометрия многоугольников',
                     'Геометрия кругов',
                     'Геометрия вписаных и описаных многоугольников',
                     'Геометрия в пространстве (стереометрия)')
        bot.send_message(message.from_user.id, "Какой раздел?", reply_markup=keyboard)
    elif message.text.lower() == 'геометрия треугольников':
        bot.send_photo(message.from_user.id, photo=open('photos/Математика/Геометрия треугольников 1.png', 'rb'), reply_markup=hideBoard)
        bot.send_photo(message.from_user.id, photo=open('photos/Математика/Геометрия треугольников 2.png', 'rb'), reply_markup=hideBoard)
        bot.send_photo(message.from_user.id, photo=open('photos/Математика/Геометрия треугольников 3.png', 'rb'), reply_markup=hideBoard)
    elif message.text.lower() == 'геометрия многоугольников':
        bot.send_photo(message.from_user.id, photo=open('photos/Математика/Геометрия многоугольников.png', 'rb'), reply_markup=hideBoard)
    elif message.text.lower() == 'геометрия треугольников':
        bot.send_photo(message.from_user.id, photo=open('photos/Математика/Геометрия кругов 1.png', 'rb'), reply_markup=hideBoard)
        bot.send_photo(message.from_user.id, photo=open('photos/Математика/Геометрия кругов 2.png', 'rb'), reply_markup=hideBoard)
        bot.send_photo(message.from_user.id, photo=open('photos/Математика/Геометрия кругов 3.png', 'rb'), reply_markup=hideBoard)
    elif message.text.lower() == 'геометрия вписаных и описаных многоугольников':
        bot.send_photo(message.from_user.id, photo=open('photos/Математика/Геометрия вписаных и описаных многоугольников.png', 'rb'), reply_markup=hideBoard)
    elif message.text.lower() == 'геометрия в пространстве (стереометрия)':
        bot.send_photo(message.from_user.id, photo=open('photos/Математика/Стереометрия.png', 'rb'), reply_markup=hideBoard)
    elif message.text.lower() == 'тригонометрия':
        keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=True)
        keyboard.add('Простая тригонометрия',
                     'Формулы двойного угла',
                     'Формулы половинного угла',
                     'Тригонометрические формулы сложения',
                     'Тригонометрические формулы преобразования суммы в произведение',
                     'Тригонометрические формулы преобразования произведения в сумму',
                     'Формулы понижения степени',
                     'Тригонометрические формулы приведения',
                     'Тригонометрическая окружность')
        bot.send_message(message.from_user.id, "Какой раздел?", reply_markup=keyboard)
    elif message.text.lower() == 'простая триганометрия':
        bot.send_photo(message.from_user.id, photo=open('photos/Математика/Простая триганометрия.png', 'rb'), reply_markup=hideBoard)
    elif message.text.lower() == 'формулы половинного угла':
        bot.send_photo(message.from_user.id, photo=open('photos/Математика/Формулы половинного угла.png', 'rb'), reply_markup=hideBoard)
    elif message.text.lower() == 'тригонометрические формулы сложения':
        bot.send_photo(message.from_user.id, photo=open('photos/Математика/Тригонометрические формулы сложения.png', 'rb'), reply_markup=hideBoard)
    elif message.text.lower() == 'тригонометрические формулы преобразования суммы в произведение':
        bot.send_photo(message.from_user.id, photo=open('photos/Математика/Тригонометрические формулы преобразования суммы в произведение.png', 'rb'), reply_markup=hideBoard)
    elif message.text.lower() == 'тригонометрические формулы преобразования произведения в сумму':
        bot.send_photo(message.from_user.id, photo=open('photos/Математика/Тригонометрические формулы преобразования произведения в сумму.png', 'rb'), reply_markup=hideBoard)
    elif message.text.lower() == 'формулы понижения степени':
        bot.send_photo(message.from_user.id, photo=open('photos/Математика/Формулы понижения степени.png', 'rb'), reply_markup=hideBoard)
    elif message.text.lower() == 'тригонометрические формулы приведения':
        bot.send_photo(message.from_user.id, photo=open('photos/Математика/Тригонометрические формулы приведения.png', 'rb'), reply_markup=hideBoard)
    elif message.text.lower() == 'тригонометрическая окружность':
        bot.send_photo(message.from_user.id, photo=open('photos/Математика/Тригонометрическая окружность.png', 'rb'), reply_markup=hideBoard)
    elif message.text.lower() == 'таблицы':
        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
        keyboard.add('Таблица умножения',
                     'Таблицы квадратов')
        bot.send_message(message.from_user.id, "Какие?", reply_markup=keyboard)
    elif message.text.lower() == 'таблица умножения':
        bot.send_photo(message.from_user.id, photo=open('photos/Математика/Таблица умножения.png', 'rb'), reply_markup=hideBoard)
    elif message.text.lower() == 'таблицы квадратов':
        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
        keyboard.add('Таблица квадратов от 1 до 100',
                     'Таблица квадратов от 100 до 200',
                     'Таблица квадратов от 200 до 300')
        bot.send_message(message.from_user.id, "Какая?", reply_markup=keyboard)
    elif message.text.lower() == 'таблица квадратов от 1 до 100':
        bot.send_photo(message.from_user.id, photo=open('photos/Математика/Таблица квадратов от 1 до 100.png', 'rb'), reply_markup=hideBoard)
    elif message.text.lower() == 'таблица квадратов от 100 до 200':
        bot.send_photo(message.from_user.id, photo=open('photos/Математика/Таблица квадратов от 100 до 200.png', 'rb'), reply_markup=hideBoard)
    elif message.text.lower() == 'таблица квадратов от 200 до 300':
        bot.send_photo(message.from_user.id, photo=open('photos/Математика/Таблица квадратов от 200 до 300.png', 'rb'), reply_markup=hideBoard)
    else:
        strings = ['Формулы',
                   'Алгебра',
                   'Геометрия',
                   'Тригонометрия',
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
                   'Время',
                   'Таблица умнождения',
                   'Таблицы квадратов',
                   'Формулы сокращенного умножения',
                   'Парабола',
                   'Свойства степеней и корней',
                   'Лагорифмы',
                   'Арифметическая прогрессия',
                   'Геометрическая прогрессия',
                   'Квадратные уравнения',
                   'Геометрия треугольников',
                   'Геометрия многоугольников',
                   'Геометрия кругов',
                   'Геометрия вписаных и описаных многоугольников',
                   'Геометрия в пространстве (стереометрия)',
                   'Простая тригонометрия',
                   'Формулы двойного угла',
                   'Формулы половинного угла',
                   'Тригонометрические формулы сложения',
                   'Тригонометрические формулы преобразования суммы в произведение',
                   'Тригонометрические формулы преобразования произведения в сумму',
                   'Формулы понижения степени',
                   'Тригонометрические формулы приведения',
                   'Тригонометрическая окружность',
                   'Таблица умножения',
                   'Таблицы квадратов',
                   'Таблица квадратов от 1 до 100',
                   'Таблица квадратов от 100 до 200',
                   'Таблица квадратов от 200 до 300']
        res = process.extractOne(message.text.lower(), strings)[0]
        bot.send_message(message.from_user.id, 'Возможно вы имелли ввиду "'+res+'"')
        message.text = res
        general_message(message)




while True:
    try:
        bot.polling(none_stop=True, interval=0)
    except:
        pass