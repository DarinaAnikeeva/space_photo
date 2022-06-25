import telegram

bot = telegram.Bot(token='5003644672:AAE_0V7VikR4A9sueeZPuP8ptME2enm5hR0')
chat_id = "@fabio_bot_1"
bot.send_message(text='Hi John!', chat_id=chat_id)