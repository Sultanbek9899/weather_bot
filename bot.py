import telebot
from telebot import types
from config import TOKEN
from service import get_weather
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    btn1 = types.KeyboardButton('Меню')
    btn2 = types.KeyboardButton('Выйти')
    markup.add(btn1, btn2)
    text = "Привет, я твой бот. Выбирай дальнейшие действия."
    bot.send_message(message.chat.id, text, reply_markup=markup)



@bot.message_handler(content_types=['text'])
def echo(message):
    get_message = message.text
    if get_message.lower() == 'меню':
        text = 'Пожалуйста выберите город температуру, которой хотите узнать'
        markup = types.InlineKeyboardMarkup(row_width=2)
        item1 = types.InlineKeyboardButton("Бишкек", callback_data='bishkek')
        item2 = types.InlineKeyboardButton("Москва", callback_data='moscow')
        item3 = types.InlineKeyboardButton("Алматы", callback_data='almaty')
        markup.add(item1, item2, item3)
        bot.send_message(message.chat.id, text, reply_markup = markup)
    elif get_message.lower() == 'выйти':
        text = 'Пока, рад был поговорить'
        bot.send_message(message.chat.id, text)

def check_temperature(temp):
    if temp > 15:
        return "На улице тепло , можете одеться свободно"
    elif temp < 5: 
        return "На улице очень холодно, следует одеть куртку"
    elif temp < 15 and temp > 5:
        return  "На улице холодновато, одентесь теплее"
    else:
        return "Неправильные данные температуру"


#реакция нажатия на кнопки в сообщении 
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'bishkek':
                data = get_weather(call.data)
                text = f'''
                    Температура в городе Бишкек: {data['temp_c']} 
                    Время в городе: {data['time']}
                    {check_temperature(data['temp_c'])}
                '''         
                bot.edit_message_text(chat_id=call.message.chat.id, text=text,message_id=call.message.message_id, reply_markup=None)
            elif call.data == 'moscow':
                data = get_weather(call.data)
                text = f'''
                    Температура в городе Москва: {data['temp_c']} 
                    Время в городе: {data['time']}
                    {check_temperature(data['temp_c'])}
                '''  
                bot.edit_message_text(chat_id=call.message.chat.id, text=text,message_id=call.message.message_id, reply_markup=None)
            elif call.data == 'almaty':
                data = get_weather(call.data)
                text = f'''
                    Температура в городе Алматы: {data['temp_c']} 
                    Время в городе: {data['time']}
                    {check_temperature(data['temp_c'])}
                ''' 
                bot.edit_message_text(chat_id=call.message.chat.id, text=text,message_id=call.message.message_id, reply_markup=None)
            # remove inline buttons
            # bot.edit_message_text(chat_id=call.message.chat.id, text='delete',message_id=call.message.message_id, reply_markup=None)
    except Exception as e:
        print(repr(e))
    

bot.polling(none_stop=True)