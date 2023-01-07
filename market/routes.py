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
        
        json1=json.loads(json_string)
        print(json1["text"])
        print(json_string['text'])
@app.route('/')
def welcome():
    return "hello,home"
