import telebot
import configs
import requests
from bs4 import BeautifulSoup as BS
from telebot import types

client = telebot.TeleBot(configs.config['token'])

# читаем сообщения и отправляем ответ
@client.message_handler(content_types = ['text'])
def get_text(message1):
   if message1.text.lower() == 'hello': # or'hi'or'yes'or'no'
       client.send_message(message1.chat.id, 'Hi, unkown user')

# r = requests.get('https://sinoptik.ua/погода-москва')
# html = BS(r.content, 'html.parser')

# for el in html.select('#bd1'):
#     t_min = el.select('.temperature .min')[0].text
#     t_max = el.select('.temperature .max')[0].text
#   #  text = el.select('.wDescription .description')[0].text
#     print(t_min + ', ' + t_max + '.')

# @client.message_handler(content_types = ['text'])
# def get_weather(message):
#    if message.text.lower() == 'pogoda':
#        client.send_message(message.chat.id, 'Привет, погода в Москве на сегодня:\n' + t_min + ', ' + t_max)


# #кнопки Inline

# @client.message_handler(commands = ['get_info', 'info'])
# def get_user_info(message):
#   markup_inline = types.InlineKeyboardMarkup()
#   item_yes = types.InlineKeyboardButton(test = 'да', callback_data='yes')
#   item_no = types.InlineKeyboardButton(test = 'нет', callback_data='no')
#   markup_inline.add(item_yes, item_no)
#   client.send_message(message.chat.id, 'Желаете доп. информацию?', reply_markup=markup_inline)


@client.callback_query_handler(func = lambda call: True)
def answer(call):
  if call.data == 'yes':
    markup_reply = types.ReplyKeyboardMarkup(resize_keyboard = True)
    item_id = types.KeyboardButton('Мой ID')
    item_username = types.KeyboardButton('Мой ник')
    markup_reply.add(item_id, item_username)
    client.send_message(call.message.chat.id, 'Нажмите одну из кнопок',
    reply_markup = markup_reply)
#  elif call.data == 'no':
#     pass 

# @client.message_handler(content_types = ['text'])
# def get_text2(message):
#    if message.text == 'Мой ID':
#     client.send_message(message.chat.id, f'Your ID: {message.from_user.id}')
#    elif  message.text == 'Мой ник':
#     client.send_message(message.chat.id, f'Your НИК: {message.from_user.first_name}')





print('Работает|working')
client.polling ()