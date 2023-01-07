from telebot import TeleBot
API_KEY='5856492498:AAEdrY7BZDG6_Bsny3oZ1X7BSfctZmLc8j8'
bot=TeleBot(API_KEY)

@bot.message_handler(func=lambda message:True)
def reply(message):
    bot.send_message(message.from_user.id ,"hello")
