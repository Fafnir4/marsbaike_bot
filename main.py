import telebot
import datetime
bot = telebot.TeleBot('5988164556:AAFq8JDgVQtpVIF_xD5NkHF77ko25_9eUXI')

day = str(datetime.date.today())
today = day[8:10]
today_int = int(today)
today_month = day[5:7]
count = 0  # 1  -  числитель
           # 2  -  знаменатель
week = ''

if today_month == "01" or today_month == "январь":
    if 9 <= today_int <= 15  or 23 <= today_int <= 29:
        count = 2
    elif 2 <= today_int <= 8 or 16 <= today_int <= 22 or 29 <= today_int <= 31:
        count = 1
    else:
        print("Ошибка")

if today_month == "02" or today_month == "февраль":
    if 1 <= today_int <= 5 or 13 <= today_int <= 19 or 27 <= today_int <= 28:
        count = 1
    elif 6 <= today_int <= 12 or 20 <= today_int <= 26:
        count = 2
    else:
        print("Ошибка")

if today_month == "03" or today_month == "март":
    if 1 <= today_int <= 5 or 13 <= today_int <= 19 or 27 <= today_int <= 31:
        count = 1
    elif 6 <= today_int <= 12 or 20 <= today_int <= 26:
        count = 2
    else:
        print("Ошибка")

if today_month == "04" or today_month == "апрель":
    if 1 <= today_int <= 2 or 10 <= today_int <= 16 or 24 <= today_int <= 30:
        count = 1
    elif 3 <= today_int <= 9 or 17 <= today_int <= 23:
        count = 2
    else:
        print("Ошибка")

if today_month == "05" or today_month == "май":
    if 1 <= today_int <= 7:
        count = 2
    elif 8 <= today_int <= 14:
        count = 1
    else:
        print("Ошибка")

if count == 1:
    week = "Числитель"
    print("Числитель")
elif count == 2:
    week = 'Знаменатель'
    print("Знаменатель")
else:
    print("Ошибка count")

'''def para():
    date_count = datetime.datetime.now()
    date_count_str = str(date_count.time())
    hour = int(date_count_str[0:2])
    minute = int(date_count_str[3:5])
    ans = ''
    if 1 <= hour <= 2:
        if 10 <= minute < 15:
            return '3/103'
        else:
            return 'НЕТУ ПАРЫ ДАМОЙ'
    elif hour == 9:
        return 'Это кто тут не реагирует?'
'''




@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "неделя" or message.text == 'Неделя':
        bot.send_message(message.chat.id, f"Привет, эта неделя {week}.")
    elif message.text == "история" or message.text == "история науки и техники" or message.text == "История":
        bot.send_message(message.chat.id, f"История Науки и Техники. \n5 кр. \nДжумагулов Сагынбек.")
    elif message.text == 'информатика' or message.text == 'Информатика' or message.text == 'информационные технологии':
        bot.send_message(message.chat.id, f"Информационные технологии. \n5 кр. \nАльбина Кубанычбековна.")
    elif message.text == "программирование" or message.text == "Программирование" or message.text == "тп":
        bot.send_message(message.chat.id, f"Технологии программирования. \n5 кр. \nЖазгул Джумадиловна.")
    elif message.text == "инфоком" or message.text == "Инфоком" or message.text == "инфокоммуникация":
        bot.send_message(message.chat.id, f"Инфокоммуникационные системы и сети. \n5 кр. \nКайратбек Дуйшокович.")
    elif message.text == "произв" or message.text == "Произв" or message.text == "пп":
        bot.send_message(message.chat.id, f"Основы производственных процессов. \n5 кр. \nЭркингуль Ахметовна")
    elif message.text == 'предметы' or message.text == 'Предметы':
        bot.send_message(message.chat.id, 'История Науки и Техники. \n5 кр. \nДжумагулов Сагынбек. \n\nИнформационные технологии. \n5 кр. \nАльбина Кубанычбековна. Технологии программирования. \n5 кр. \nЖазгул Джумадиловна.\n\nИнфокоммуникационные системы и сети. \n5 кр. \nКайратбек Дуйшокович.\n\nОсновы производственных процессов. \n5 кр. \nЭркингуль Ахметовна')
    elif message.text == 'пн' or message.text == 'Пн' or message.text == 'понедельник' or message.text == 'Понедельник':
        bot.send_message(message.chat.id, '*9:30-10:50  Лк. 5/13 Технологии програмирования\n*11:00-12:20   Пр. Немка\n*13:00-14:20   Физра\n*14:30-15:50    Лб. 5/36 Инфоком. системы')
    elif message.text == 'вт' or message.text == 'Вт' or message.text == 'вторник' or message.text == 'Вторник':
        bot.send_message(message.chat.id, '*13:00-14:20   Пр. 3/101 Основы произв. процессов\n*14:30-15:50   Лб. 5/36 Инфоком. системы\n      Лб. 3/105 Информационные технологии\n*16:00-17:20   Чис. Лб. 5/36 Инфоком. системы\n      Чис. Лб. 3/105 Информационные Технологии')
    elif message.text == 'ср' or message.text == 'Ср' or message.text == 'среда' or message.text == 'Среда':
        bot.send_message(message.chat.id, '*11:00-12:20   Пр. Немка\n*13:00-14:20   Лк. 3/201 Основы произв. процессов\n*14:30 - 15:50   Лб. 3/201 Основы произв. процессов\n*16:00-17:20   Пр. 3/201 Основы произв. процессов')
    elif message.text == 'чт' or message.text == 'Чт' or message.text == 'четверг' or message.text == 'Четверг':
        bot.send_message(message.chat.id, '*8:00-9:20   Лб. 3/105 Информационные Технологии\n*9:30-10:50   Лк. 5/13 Инфоком. системы\n*11:00 - 12:20   Знам. Лб. 3/105 Информационные Технологии\n      Числ. Лк. 2/606 Информационные Технологии\n*13:00 - 14:20   Физра')
    elif message.text == 'пт' or message.text == 'Пт' or message.text == 'пятница' or message.text == 'Пятница':
        bot.send_message(message.chat.id, '*8:00-9:20   Немка\n*9:30-10:50   Лк. 3/106 История науки и техники\n*11:00-12:20   Пр. 3/106 История науки и техники\n*13:00-14:20   Числ. Лк. 3/106 История науки и техники')
    elif message.text == 'сб' or message.text == 'Сб' or message.text == 'суббота' or message.text == 'Суббота':
        bot.send_message(message.chat.id, '*8:00-9:20   Лб. 5/36 Технологии программирования\n*9:30-10:50   Лб. 5/36 Технологии программирования\n*11:00-12:20   Лб. 5/36 Технологии программирования\n*13:00-14:20   Лб. 5/36 Технологии программирования')
    elif message.text == 'адил':
        bot.send_message(message.chat.id, 'гейний')
           #elif message.text == "аудитория":
    #    bot.send_message(message.chat.id, para()) .!.


bot.polling(none_stop=True, interval=0)
