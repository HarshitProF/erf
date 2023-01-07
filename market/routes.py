from market import app
from flask import request
from telebot.types import Update
from bot import bot
API_KEY='5856492498:AAEdrY7BZDG6_Bsny3oZ1X7BSfctZmLc8j8'
url='/'+API_KEY
@app.route(url,methods=['POST'])
def handle():
    if request.method=="POST":
        json_string=request.get_data().decode('utf-8')
        print(json_string)
        update=Update.de_json(json_string)
        bot.process_new_updates(update)
        return json_string
@app.route('/')
def welcome():
    return "hello,home"
