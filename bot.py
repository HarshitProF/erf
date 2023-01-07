from telebot import TeleBot
API_KEY="8jd"
bot=TeleBot(API_KEY)

@bot.message_handler(func=lambda :True)
def reply(message):
    bot.send_message(message.from_user.id ,"hello")