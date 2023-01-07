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
        return "done"
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    text=str(message.text)
    messa=text.split("\n")
    data={
        "dat":messa[0],
        "pair":messa[2].split(":")[1],
        "type":messa[3],
        "leverage":messa[4].split(":")[1],
        "entry":messa[5].split(":")[1],
        "tagets":[float(messa[7].split(":")[1]),float(messa[8].split(":")[1]),float(messa[9].split(":")[1]),float(messa[10].split(":")[1]),float(messa[11].split(":")[1]),float(messa[12].split(":")[1]),(messa[13].split(":")[1])],
        "stoploss": messa[15].split(":")[1]
    }
    message1=f"✨{data['pair']}\n\n🎗 Trade Type={data['type']}\n\n💫 Leverage={data['leverage']}\n\n⚡️ Entry={data['entry']}\n\n❌ StopLoss={data['stoploss']}\n\n❎ Take profit={data['tagets']}"
    message2=f"📍 {data['pair']}\n\n🏹 Signal Type:- {data['type']}\n\n💫Leverage: {data['leverage']}\n\n👉 Entry Targets:- {data['entry']}\n\n🎯 Profit Targets:\n1) {data['tagets'][0]}\n2) {data['tagets'][1]}\n3) {data['tagets'][2]}\n4) {data['tagets'][3]}\n5) {data['tagets'][4]}\n6) {data['tagets'][5]}\n7) {data['tagets'][6]}\n\n🛑 Stop Target: {data['stoploss']} "
    message3=f"⚡️💫 {data['pair']} 💫⚡️\n\n[{data['type']}]:{data['entry']}\n\n✨🎯 TARGETS ✨🎯\n\n1.Goal👉 {data['tagets'][0]}\n2.Goal👉 {data['tagets'][1]}\n3.Goal👉 {data['tagets'][2]}\n4.Goal👉 {data['tagets'][3]}\n5.Goal👉 {data['tagets'][4]}\n6.Goal👉 {data['tagets'][5]}\n7.Goal👉 {data['tagets'][6]}\n\nSL🛑:- {data['stoploss']}\n\n🎗 LEVERAGE:- {data['leverage']}"
    bot.send_message(message.from_user.id ,text=message1)
    bot.send_message(message.from_user.id ,text=message2)
    bot.send_message(message.from_user.id ,text=message3)
@app.route('/')
def welcome():
    return "hello,home"
