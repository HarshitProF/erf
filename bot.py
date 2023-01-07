from telebot import TeleBot
bot=TeleBot(API_KEY)

@bot.message_handler(func=lambda :True)
def reply(message):
    bot.send_message(message.from_user.id ,"hello")
