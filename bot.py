import telebot
from decouple import config

BOT_TOKEN = config('BOT_TOKEN')

bot = telebot.TeleBot(BOT_TOKEN)

def isMSg(message): 
    return True

@bot.message_handler(commands=["start","help"])
def welcome(message):
    bot.send_message(message.chat.id, "welcome to My Bot")

@bot.message_handler(func=isMSg)         
def reply(message):
    bot.reply_to(message, "that not command")
    
bot.polling()
