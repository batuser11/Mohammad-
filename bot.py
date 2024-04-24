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

def isMsg(message):
    return message.text.isdigit()
@bot.message_handler(func=isMsg)
def send_user_info(message):
    user_id = int(message.text)
    user_info = bot.get_chat_member(message.chat.id, user_id)
    user_first_name = user_info.user.first_name
    user_username = user_info.user.username
    bot.reply_to(message, f"username: {user_first_name}\name: @{user_username}")

bot.polling()
