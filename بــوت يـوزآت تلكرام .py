import os
from telebot import types
import telebot
import requests
import random


token = '6883060536:AAEI02peYqeSY93kxHk0Re4X0dUD_xjz94E'
#هنا توكنك داخل دبل كتيشن

bot = telebot.TeleBot(token)

bo = types.InlineKeyboardButton(text='بــدء آلصـيد', callback_data='start')
me = types.InlineKeyboardButton(text='قنـاتـي', url='https://t.me/PYTHOU')

@bot.message_handler(commands=['start'])
def start(message):
	m = types.InlineKeyboardMarkup(row_width=2)
	m.add(bo, me)
	bot.send_message(message.chat.id, f"<b> هآ گوآد > {message.from_user.first_name} .</b>",parse_mode='html',reply_markup=m)

@bot.callback_query_handler(func=lambda call: True)
def qwere(call):
	if call.data == 'start':
		li(call.message)

def li(message):
    error = 0
    done = 0
    no=0
    koko = bot.reply_to(message, "<b>جاري الصيد..</b>", parse_mode='html').message_id

    while True:
        us = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ_1234567890'
        user1 = ("".join(random.choice(us)for i in range(1)))
        user2 = ("".join(random.choice(us)for i in range(1)))
        user = user1+user1+user1+user1+user1+user2
        
        req = requests.get(f'https://t.me/{user}').text
        if '"robots"' in req:
        	headers = {
    'authority': 'fragment.com',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'ar-IQ,ar;q=0.9,en-US;q=0.8,en;q=0.7',
     'cookie': 'stel_ssid=b2a6d1116a8f8a31fb_1331735887277205031; stel_dt=-180',
    'referer': 'https://fragment.com/?query=py_50',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
    'x-aj-referer': 'https://fragment.com/?query=py_50',
    'x-requested-with': 'XMLHttpRequest'}

        	r = requests.get(f'https://fragment.com/username/{user}',headers=headers).text
        	if '?query' in r:
        	   done += 1
        	   bot.send_message(message.chat.id, f"<b>Good user\nuser : @{user}</b>", parse_mode="html")  
        	else:
        		error += 1
        		
        else:
        	no += 1
        	   
        	ms = types.InlineKeyboardMarkup(row_width=2)
        	
        	v1 = types.InlineKeyboardButton(f"Hit ➜ [ {done} ]", callback_data='mn')
        	v2 = types.InlineKeyboardButton(f"Bad ➜ [ {error} ]", callback_data='mnm')
        	Checkr = types.InlineKeyboardButton(f"user ➜ [ @{user} ]", callback_data='asnm')
        	nno = types.InlineKeyboardButton(f"Erorr ➜ [ {no} ]", callback_data='asm')
        	v3 = types.InlineKeyboardButton(f"uvuxv", url="https://t.me/PY_50", callback_data='tynn')
        	v4 = types.InlineKeyboardButton(f"@PYTHOU", url="https://t.me/PYTHOU", callback_data='mnn')
        	ms.add(v1,v2)
        	ms.add(Checkr,nno)
        	ms.add(v4,v3)
        	
        	
        	bot.edit_message_text(chat_id=message.chat.id, message_id=koko, text='<b>Start Fishing By uvuxv ....⌛</b>', parse_mode='html', reply_markup=ms)
            
        

print(f'Go Bot starting \ntoken : {token}')

bot.polling(True)


#ZAID MOD 
