import os
import requests
from telegram import Bot

TOKEN = os.getenv("TOKEN")
EMBY_URL = " http://192.168.4.51:8096"
LIBRARY_ID = "d41d8cd98f00b204e9800998ecf8427e"

bot = Bot(TOKEN)

def get_movies():
    url = f"{EMBY_URL}/emby/Library/Items?Recursive=true&IncludeItemTypes=Movie&Fields=Path&UserId=96b8c2eab8834e60b00310dd9a4d3031&ParentId={LIBRARY_ID}"
    response = requests.get(url)
    movies = []
    for item in response.json()["Items"]:
        movies.append(item["Path"])
    return movies

def start(update, context):
    movies = get_movies()
    message = "Here are your movies:\n\n"
    for movie in movies:
        message += f"{movie}\n"
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)

from telegram.ext import CommandHandler

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
