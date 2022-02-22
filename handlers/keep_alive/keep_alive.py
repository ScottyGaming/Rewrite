from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "Booobaaa Bot is Alive! Copy Paste This Invite link to invite it to your server! : https://discord.com/oauth2/authorize?client_id=910852830884147200&permissions=8&scope=bot"

def run():
  app.run(host='0.0.0.0',port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()