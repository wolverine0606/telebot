import requests
import telebot
from auth_data import token
from datetime import datetime


# communication with client
def telegram_bot(token):
    bot = telebot.TeleBot(token)

    #first communication with client
    @bot.message_handler(commands=['start'])
    def start_message(message):
        bot.send_message(message.chat.id, "Hello friend! Write the 'price' to find out the cost of BTC")

    @bot.message_handler(content_types=['text'])
    def send_text(message):
        if message.text.lower() == 'price':
            try:
                req = requests.get('https://yobit.net/api/3/ticker/btc_usd')
                responce = req.json()
                sell_price = responce['btc_usd']['sell']
                bot.send_message(
                    message.chat.id,
                    f"{datetime.now().strftime('%Y-%m-%d %H-%M')}\n Sell BTC PRICE: {sell_price}"
                )
            except Exception as ex:
                print(ex)
                bot.send_message(message.chat.id, 'Damn... Something was wrong')

        else:
            bot.send_message(message.chat.id, 'What??? Check the command dude!')

    bot.polling()


if __name__ == '__main__':
    telegram_bot(token)
