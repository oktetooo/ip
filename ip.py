import json
import os
import sys
import time

    import telebot
    from telebot import *
    from user_agent import generate_user_agent
    import colorama
    import requests

def slow(M):
    for c in M + "\n":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1. / 300)
        
def cls():
    os.system('cls' if os.name == 'nt' else 'clear')
    
YELLOW = colorama.Fore.YELLOW
BLUE = colorama.Fore.BLUE
GREEN = colorama.Fore.GREEN
WHITE = colorama.Fore.WHITE
CYAN = colorama.Fore.CYAN
RED = colorama.Fore.RED
MAGENTA = colorama.Fore.MAGENTA

logo = f'''
      {YELLOW}8888888b.{MAGENTA}88888888888
      {YELLOW}888  "Y88b   {MAGENTA}888
      {YELLOW}888    888   {MAGENTA}888
      {YELLOW}888    888   {MAGENTA}888
      {YELLOW}888    888   {MAGENTA}888
      {YELLOW}888    888   {MAGENTA}888
      {YELLOW}888  .d88P   {MAGENTA}888
      {YELLOW}8888888P"    {MAGENTA}888 

    {MAGENTA}❴ {WHITE}Code By MOSTAFA PRO {MAGENTA}❵
{YELLOW}╭─{MAGENTA}────────────────────────────{YELLOW}╮ 
{MAGENTA}│ {WHITE}⁕ Channel › DEVElOPERS TEAM {MAGENTA}│
{MAGENTA}│ {WHITE}⁕ Link    › @D_C_D_D        {MAGENTA}│
{MAGENTA}│ {WHITE}⁕ Author  › MOSTAFA PRO     {MAGENTA}│
{MAGENTA}│ {WHITE}⁕ Link    › @m_p_r_o        {MAGENTA}│
{YELLOW}╰─{MAGENTA}────────────────────────────{YELLOW}╯
'''

def get_info_ip(ip: str) -> str:
    request = json.loads(requests.get(f"https://ipinfo.io/widget/demo/{ip}", headers={
        'Host': 'ipinfo.io',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
        'sec-ch-ua-mobile': '?1',
        'save-data': 'on',
        'user-agent': str(generate_user_agent()),
        'sec-ch-ua-platform': '"Android"',
        'content-type': 'application/json',
        'accept': '*/*',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://ipinfo.io/',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7',
        'cookie': 'flash=',
        'cookie': 'bento_visitor_id=d0224ad9-b83a-4103-a8e6-aa794b0fc1da',
        'cookie': 'bento_visit_id=b70e5bfe-8341-43e5-a46c-84a3c14cf2e5',
        'cookie': 'bento_events=%5B%7B%22id%22%3A%22a1203021-2f6a-4d31-b42d-06718983bd77%22%2C%22site%22%3A%220d66e7448ad29ad69828d1d4201299a2%22%2C%22visitor%22%3A%22d0224ad9-b83a-4103-a8e6-aa794b0fc1da%22%2C%22visit%22%3A%22b70e5bfe-8341-43e5-a46c-84a3c14cf2e5%22%2C%22type%22%3A%22%24view%22%2C%22date%22%3A%22Wed%2C%2022%20Jun%202022%2015%3A46%3A15%20GMT%22%2C%22browser%22%3A%7B%22user_agent%22%3A%22Mozilla/5.0%20%28Linux%3B%20Android%208.0.0%3B%20SM-G930V%29%20AppleWebKit/537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome/96.0.4664.92%20Mobile%20Safari/537.36%22%7D%2C%22page%22%3A%7B%22url%22%3A%22https%3A//ipinfo.io/%22%2C%22queryString%22%3A%22%22%2C%22anchor%22%3A%22%22%2C%22host%22%3A%22ipinfo.io%22%2C%22path%22%3A%22/%22%2C%22protocol%22%3A%22https%3A%22%2C%22title%22%3A%22Comprehensive%20IP%20addrequests%20data%2C%20IP%20geolocation%20API%20and%20database%20-%20IPinfo.io%22%2C%22referrer%22%3A%22%22%7D%2C%22identity%22%3A%7B%7D%7D%5D'
    }).text)
    try:
        try:
            ip = request["data"]["ip"]
        except KeyError:
            ip = "Null"
        try:
            name = request["data"]["name"]
        except KeyError:
            name = "Null"
        try:
            city = request["data"]["city"]
        except KeyError:
            city = "Null"
        try:
            country = request["data"]["country"]
        except KeyError:
            country = "Null"
        try:
            isp = request["data"]["region"]
        except KeyError:
            isp = "Null"
        try:
            region = request["data"]["org"]
        except KeyError:
            region = "Null"
        try:
            timezone = request["data"]["timezone"]
        except KeyError:
            timezone = "Null"
        try:
            postal = request["data"]["postal"]
        except KeyError:
            postal = "Null"
        try:
            asn = request["data"]["asn"]["asn"]
        except KeyError:
            asn = "Null"
        try:
            asn_name = request["data"]["asn"]["name"]
        except KeyError:
            asn_name = "Null"
        try:
            domain = request["data"]["asn"]["domain"]
        except KeyError:
            domain = "Null"
        try:
            route = request["data"]["asn"]["route"]
        except KeyError:
            route = "Null"
        try:
            company_name = request["data"]["company"]["name"]
        except KeyError:
            company_name = "Null"
        try:
            vpn = request["data"]["privacy"]["vpn"]
        except KeyError:
            vpn = "Null"
        try:
            proxy = request["data"]["privacy"]["proxy"]
        except KeyError:
            proxy = "Null"
        try:
            service = request["data"]["privacy"]["service"]
        except KeyError:
            service = "Null"
        try:
            hosting = request["data"]["privacy"]["hosting"]
        except KeyError:
            hosting = "Null"
        try:
            address = request["data"]["abuse"]["address"]
        except KeyError:
            address = "Null"
        try:
            email = request["data"]["abuse"]["email"]
        except KeyError:
            email = "Null"
        try:
            phone = request["data"]["abuse"]["phone"]
        except KeyError:
            phone = "Null"
        
        return f"""──────────────────
✅│ Ip : {ip} 
──────────────────
✜│ Name : {name}
✜│ City : {city}
✜│ Country : {country}
✜│ Email : {email}
✜│ Phone : {phone}
✜│ Proxy : {proxy}
✜│ Vpn : {vpn}
✜│ Service : {service}
✜│ Hosting : {hosting}
✜│ Address : {address}
✜│ Timezone : {timezone}
✜│ Domain : {domain}
✜│ Company Name : {company_name}
✜│ Postal : {postal}
✜│ Region : {region}
✜│ Route : {route}
✜│ Isp : {isp}
✜│ Asn : {asn}
✜│ Asn Name : {asn_name}
──────────────────
👨🏻‍💻│ Developer : @M_P_R_O
⚒️│ Channel : @D_C_D_D
──────────────────"""
    
    except:
        return f"""────────────────── 
❌│ Ip : {ip} 
──────────────────
👨🏻‍💻│ Developer : @M_P_R_O
⚒️│ Channel : @D_C_D_D
──────────────────"""

cls()
slow(logo)
bot = telebot.TeleBot('5542067766:AAEw4Qw67wxczRDDn-ro9YMNDsHqFbLKHH0')
print(f'{MAGENTA}❴{GREEN}✜ {MAGENTA}❵ {WHITE}Done')
@bot.message_handler(commands=['start'])
def welcome(message):
    channel = types.InlineKeyboardButton(text=" ⚒️ Channel Developer ", url="https://t.me/D_C_D_D")
    start = types.InlineKeyboardButton(text=" 📮 Start ", callback_data="start")
    programmer = types.InlineKeyboardButton(text=" 👨🏻‍💻 Developer ", url="https://t.me/M_P_R_O")
    Keyboards = types.InlineKeyboardMarkup()
    Keyboards.row_width = 2
    Keyboards.add(start,  programmer,  channel)
    bot.send_message((message.chat.id), text=f"🌹│ Hi {message.from_user.first_name} in Bot info ip \n🔰│ Please Click", reply_to_message_id=(message.message_id), reply_markup=Keyboards)
    
@bot.callback_query_handler(func=lambda call: True)
def mostafa(call):
    if call.data == "start":
        messages = bot.reply_to(call.message, "✏│ Enter ip")
        bot.register_next_step_handler(messages, run)

def run(message):
    messages = bot.send_message(message.chat.id, f'📮│ Starting ⏳ Please Wait ...')
    time_imog = list("⌛⏳⌛⏳⌛⏳⌛")
    for i in range(len(time_imog)):
        bot.edit_message_text(text=f'📮│ Starting {time_imog[i]} Please Wait ...', chat_id=int(message.chat.id), message_id=messages.message_id)
        time.sleep(0.6)
    bot.send_message(message.chat.id, get_info_ip(message.text))
    

if __name__ == "__main__":
    while True:
        try:
            bot.polling(True)
            break
        except Exception as ex:
            print(f"Error polling : {ex}")
            telebot.logger.error(ex)
            continue
