import date_func, creator, telebot
days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
pares = ["нет пар!!!!","всего одна пара","две пары","три пары","четыре пары","пять пар:(","шесть пар:(((("]
week = ["нечётная", "чётная"]

token = ''
bot = telebot.TeleBot(token)

lessons = creator.get_lessons()

# Выдает расписание конкретного дня в расписании
def create_output(day_num,week_num=-1):
	count_lessons = 1
	day_lessons = lessons[day_num]
	output_str = f"{days[day_num%7]}, {week[day_num//7]} неделя.\n\n_____У тебя {pares[len(day_lessons)-day_lessons.count('')]}_____\n"
	if week_num != -1:
		output_str = f"________НЕДЕЛЯ НОМЕР {week_num}_________" + output_str

	for i in range(len(day_lessons)):
		if type(day_lessons[i]) == type([]):
			output_str = output_str + f"=> Пара №{count_lessons}: {' '.join(day_lessons[i])}\n"
		count_lessons+=1
	return output_str





@bot.message_handler(commands=['today'])
def today_lessons(message):
	day,week = date_func.curent_day()
	count_lessons = 1
	output = create_output(day,week)
	bot.send_message(message.chat.id,output)

@bot.message_handler(commands=['tomorrow'])
def tomorrow_lessons(message):
	day,week = date_func.tomorrow_date()
	output = create_output(day,week)
	bot.send_message(message.chat.id,output)





@bot.message_handler(commands=['monday']) # Первый день в неделе => индексы в списке дней 0 и 7
def today_lessons(message):	
	week = date_func.curent_week()
	bot.send_message(message.chat.id,f"СЕЙЧАС {week}-АЯ НЕДЕЛЯ!")

	odd_week_output = create_output(0)
	bot.send_message(message.chat.id,odd_week_output)
	honest_week_output = create_output(7)
	bot.send_message(message.chat.id,honest_week_output)

@bot.message_handler(commands=['tuesday']) # 1 и 8
def today_lessons(message):	
	week = date_func.curent_week()
	bot.send_message(message.chat.id,f"СЕЙЧАС {week}-АЯ НЕДЕЛЯ!")

	odd_week_output = create_output(1)
	bot.send_message(message.chat.id,odd_week_output)
	honest_week_output = create_output(8)
	bot.send_message(message.chat.id,honest_week_output)

@bot.message_handler(commands=['wednesday']) # 2 и 9
def today_lessons(message):	
	week = date_func.curent_week()
	bot.send_message(message.chat.id,f"СЕЙЧАС {week}-АЯ НЕДЕЛЯ!")

	odd_week_output = create_output(2,week)
	bot.send_message(message.chat.id,odd_week_output)
	honest_week_output = create_output(9,week)
	bot.send_message(message.chat.id,honest_week_output)

@bot.message_handler(commands=['thursday']) # 3 и 10
def today_lessons(message):	
	week = date_func.curent_week()
	bot.send_message(message.chat.id,f"СЕЙЧАС {week}-АЯ НЕДЕЛЯ!")

	odd_week_output = create_output(3)
	bot.send_message(message.chat.id,odd_week_output)
	honest_week_output = create_output(10)
	bot.send_message(message.chat.id,honest_week_output)

@bot.message_handler(commands=['friday']) # 4 и 11
def today_lessons(message):	
	week = date_func.curent_week()
	bot.send_message(message.chat.id,f"СЕЙЧАС {week}-АЯ НЕДЕЛЯ!")

	odd_week_output = create_output(4)
	bot.send_message(message.chat.id,odd_week_output)
	honest_week_output = create_output(11)
	bot.send_message(message.chat.id,honest_week_output)

@bot.message_handler(commands=['saturday']) # 5 и 12
def today_lessons(message):	
	week = date_func.curent_week()
	bot.send_message(message.chat.id,f"СЕЙЧАС {week}-АЯ НЕДЕЛЯ!")

	odd_week_output = create_output(5)
	bot.send_message(message.chat.id,odd_week_output)
	honest_week_output = create_output(12)
	bot.send_message(message.chat.id,honest_week_output)

@bot.message_handler(commands=['start',"help"])
def start_message(message):
	bot.send_message(message.chat.id,"Здесь вы сможете узнать расписание группы БИСО-01-22\n\n____В меню находится список команд бота\n____Также, отправив дату в формате DD.MM.YYYY, вы можете получть расписание конкретной даты в учебном семестре")

bot.infinity_polling()


