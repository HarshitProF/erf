from flask import Flask
app=Flask(__name__)
from market import routes
from bot import bot

