import telebot
import os
import random
from dotenv import load_dotenv  # импортировали модуль для работы со средой окружения

load_dotenv()  # грузим переменные среды
tok = os.environ.get("TOK")

BotCore = telebot.TeleBot(tok)
items = {"Старая лопата": 6, "бронзовые часы": 14, "червячок": 0.3, "купон на авито": 4, "бутылка из-под пива": 0.5,
         "черкаш": 1,
         "клавиша": 0.1, "кубик-рубика": 2, "весло": 3, "консерва": 1.5, "мангал": 4.5, "кепка": 2,
         "карта Каргастана": 0.9, "корзина": 1.5,
         "ржавый тромбон": 3.5, "колокол": 3.7, "треснутый бокал": 2, "ветка берёзы": 0.2,
         "Золотая древне-русская монета": 15,
         "Египетский меч": 81, "карта сокровищ": 30, "пиратская шляпа": 9, "лунный камень": 150, "кость динозавра": 448,
         "древний рог демона": 12000, "Super_Promo2024": 3000}
welcome = '''Привет археолог! Добро пожаловать на твой первый рабочий день на раскопках, Вся твоя работа это -вскапывать
           землю, песок и всё остальное. Мы в поисках объекта имеющего великую силу.. а так же название "Промокод"
           приятного рабочего дня, а так же воду вы должны приносить с собой сами, удачи. (Что бы начать раскопки вызовите команду "/menu"'''


@BotCore.message_handler(commands=["start"])
def hello(message):
    BotCore.send_message(message.chat.id, text=welcome)


def makeMenu():  # Создание клавиатуры с кнопкой "копать"
    keyBoard = telebot.types.ReplyKeyboardMarkup()
    button1 = telebot.types.KeyboardButton("Копать")
    keyBoard.add(button1)
    return keyBoard


@BotCore.message_handler(commands=["menu"])
def menu(message):
    keyBoard = makeMenu()
    BotCore.send_message(message.chat.id, text="Меню", reply_markup=keyBoard)


money = 0


@BotCore.message_handler(content_types=["text"])
def grass(message):
    global money

    if message.text == "Копать" or message.text == "Продолжить копать" or message.text == "Не использовать":
        item = random.choices(list(items.keys()),  # Выбирает случайный ключ из словаря со своей вероятностью
                              weights=[19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 8,
                                       16, 17, 7, 4, 1, 99])[0]
        global ISE
        ISE = 0
        money += items[item]
        keyboard = makeMenu()
        BotCore.send_message(message.chat.id, text=f"ваш текущий баланс {money}$", reply_markup=keyboard)
        BotCore.send_message(message.chat.id, text=item)
        if item == "древний рог демона":

            ISE += 2
        if item == "Super_Promo2024":
            BotCore.send_message(message.chat.id, text="Ура, поздравляю ты откопал то что мы искали уже 57 лет."
                                                       " Теперь, наша компания закрывается,"
                                                       " и выбор остаётся за тобой,"
                                                       " ты можешь быть в поиске ещё более дорогих вещей, Или же,"
                                                       "Уйти со своими деньгами, Удачи!")

            Finalboard = telebot.types.ReplyKeyboardMarkup()
            button1 = telebot.types.KeyboardButton("Продолжить копать")
            button2 = telebot.types.KeyboardButton("Уйти довольным")
            button3 = telebot.types.KeyboardButton("Другое действие")
            Finalboard.add(button1, button2, button3)
            BotCore.send_message(message.chat.id, text="Твой выбор", reply_markup=Finalboard)

    if message.text == "Другое действие":
        secretBoard = telebot.types.ReplyKeyboardMarkup()
        button1 = telebot.types.KeyboardButton("Использовать рог демона")
        button2 = telebot.types.KeyboardButton("Не использовать")
        secretBoard.add(button1, button2)
        BotCore.send_message(message.chat.id, text="...", reply_markup=secretBoard)



    if message.text == "Уйти довольным":
        money = 0
        BotCore.send_message(message.chat.id,
                             text="После полученных денег,"
                                  " ты разорвал контракт о сотрудничестве,"
                                  "возвращаясь домой, ты осознал что работал не ради "
                                  "удовольствия,"
                                  "а ради промокода с которым ты свернул на соседнею улицу и "
                                  "зашел в магазин 'Яблочко' и скупил все диваны Ulto pro + "
                                  "с шёлковистым покрытием, по скидке в 88,8%",
                             reply_markup=telebot.types.ReplyKeyboardRemove())
    if message.text == "Использовать рог демона" and ISE >0:
        BotCore.send_message(message.chat.id, text="Достав рог демона, ты уранил его на землю..."
                                                   " При первом прикосновении с землёй,"
                                                   " рог треснул и из него шквалом хлынул чёрный дым,"
                                                   " закрывший собой всю ближайшую местность,"
                                                   " после рассеивания дыма, ты увидел странную тень на песке,"
                                                   " подняв голову выше ты заметил сущность,"
                                                   " имеющею странный окрас и человеческое тело сложение,"
                                                   "отличалась она наличием хвоста и странными масками у головы,"
                                                   " его вид было тяжело описать из за отсвета солнца,"
                                                   "после 3 - 4 секунд столкновения взглядом с ним,"
                                                   " весь горизонт вновь окрасился в чёрный,"
                                                   "я не видел ни чего, и ни кого... спустя буквально 7 секунд,"
                                                   " смыслить о чём то становилось всё тяжелее и тяжелее,"
                                                   "в конце мой разум совсем отключился.. я погрузился в сон..."
                                                   "и больше так ни кто и не просыпался...",
                             reply_markup=telebot.types.ReplyKeyboardRemove())




BotCore.infinity_polling()
