from market import app
from flask import request,jsonify
from telebot.types import Update
from bot import bot
import json
API_KEY='5856492498:AAEdrY7BZDG6_Bsny3oZ1X7BSfctZmLc8j8'
url='/'+API_KEY
@app.route(url,methods=['POST'])
def handle():
    if request.method=="POST":
        json_string=request.get_data().decode('utf-8')
        update=Update.de_json(json_string)
        bot.process_new_updates([update])
        json1=json.loads(json_string)
        message=json1['message']['text']
        messa=message.split("\n")
        data={
        "dat":messa[0],
        "pair":messa[2].split(":")[1],
        "type":messa[3],
        "leverage":messa[4].split(":")[1],
        "entry":messa[5].split(":")[1],
        "tagets":[float(messa[7].split(":")[1]),float(messa[8].split(":")[1]),float(messa[9].split(":")[1]),float(messa[10].split(":")[1]),float(messa[11].split(":")[1]),float(messa[12].split(":")[1]),(messa[13].split(":")[1])],
        "stoploss": messa[15].split(":")[1]
        }
        print(data)
        bot.send_message(message['message']['from']['id'],text="hi")
        return "done"
@app.route('/')
def welcome():
    return "hello,home"
