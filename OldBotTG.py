import telebot
import random
bot = telebot.TeleBot("*")
@bot.message_handler(commands= ["menu"])
def menu(message):
    keyBoard = telebot.types.ReplyKeyboardMarkup(resize_keyboard= True)


    button1 = telebot.types.KeyboardButton("Рандомное число")
    button2 = telebot.types.KeyboardButton("генератор пароля")
    button3 = telebot.types.KeyboardButton("?")
    keyBoard.add(button1,button3,button2)
    bot.send_message(message.chat.id, text= "Меню", reply_markup= keyBoard)




#@bot.message_handler(content_types= ["text"])
#def password(message):
    #if message.text == "генератор пароля":
        #currentPIN = random.sample(range(100000, 999999), 6)
        #bot.send_message(message.chat.id, text= currentPIN)

@bot.message_handler(content_types= ["text"])
def text(message):
    if message.text == "генератор пароля":
        number2 = random.randint(100000, 999999)
        bot.send_message(message.chat.id, text= str(number2))

    if message.text == "Рандомное число":
        number = random.randint(0, 10)
        bot.send_message(message.chat.id, text= str(number))

    if message.text == "?":
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard= True)
        button4 = telebot.types.KeyboardButton("Собани")
        button5 = telebot.types.KeyboardButton("шлёпы")
        button6 = telebot.types.KeyboardButton("без коментариев...")
        keyboard.add(button4, button5, button6)
        bot.send_message(message.chat.id, text="?", reply_markup=keyboard)
    if message.text == "Собани":

        bg = open("pictures/sob1.png", "rb")
        bg2 = open("pictures/sob2.png", "rb")
        bg3 = open("pictures/sob3.png", "rb")
        bg4 = open("pictures/sob4.png", "rb")
        photos = [bg, bg2, bg3, bg4]
        randPh = random.choice(photos)
        bot.send_photo(message.chat.id, randPh)


    if message.text == "шлёпы":
        fp = open("pictures/flo.png", "rb")
        fp2 = open("pictures/flo2.png", "rb")
        fp3 = open("pictures/flo3.png", "rb")
        photos2 = [fp, fp2, fp3]
        randFL = random.choice(photos2)
        bot.send_photo(message.chat.id, randFL)

    if message.text == "без коментариев...":
        rd = open("pictures/ran.png", "rb")
        rd2 = open("pictures/ran2.png", "rb")
        rd3 = open("pictures/ran3.png", "rb")
        photos3 = [rd, rd2, rd3]
        randBZ = random.choice(photos3)
        bot.send_photo(message.chat.id, randBZ)


bot.polling(non_stop=True)