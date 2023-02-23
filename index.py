import os
import requests
import json
from telegram import Bot

TOKEN = os.getenv("5993830966:AAEA0M_JCcFSlToHfUZzJfIWqJs7Yl8gfIA")
EMBY_SERVER = " http://192.168.4.51:8096"
EMBY_API_KEY = os.getenv("74aeed3e4f0d4161b3e995de01280e37")

bot = Bot(TOKEN)

def get_movie_list():
    headers = {
        "X-Emby-Token": EMBY_API_KEY,
        "Accept": "application/json"
    }
    url = EMBY_SERVER + "/emby/Users/Public/Items"
    response = requests.get(url, headers=headers)
    data = json.loads(response.text)
    movie_list = []
    for item in data:
        if item["Type"] == "Movie":
            movie_list.append(item["Name"])
    return movie_list

def send_movie_list():
    movie_list = get_movie_list()
    if not movie_list:
        bot.send_message(chat_id=<YOUR_CHAT_ID>, text="No movies found on Emby server")
    else:
        message = "List of movies on Emby server:\n\n"
        for movie in movie_list:
            message += "- " + movie + "\n"
        bot.send_message(chat_id=<YOUR_CHAT_ID>, text=message)

if __name__ == "__main__":
    send_movie_list()
