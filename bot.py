import telebot
from decouple import config

BOT_TOKEN = config('BOT_TOKEN')

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=["start","help"])
def welcome(message):
    bot.send-message(message.chat.id,"welcome to My Bot")
    #answer all msg
    def isMSg(message): 
        return True
    
@bot.message_handler(func=isMSg)         # type: ignore
def reply(message):
        bot.reply_to(message,"that not command")
bot.polling()