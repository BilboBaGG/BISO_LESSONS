import datetime as dt

FIRST_DAY = dt.date(2022,8,29) # Дата первого понедельника в учебном году, от которого будет рассчитываться расписание

# Функции вернут индекс дня в массиве из расписания (день недели в зависимости от даты) и номер недели

# Вывод сегодняшней недели
def curent_week():
	date = dt.date.today()
	delta = date - FIRST_DAY
	return delta.days//7 + 1 

# Для сегодняшнего дня
def curent_day():
	now = dt.date.today()
	if now.year >= 2023:
		return "BIG_YEAR",None
	#if now < FIRST_DAY + dt.timedelta(days=3):
	#	return "NO_YEAR"
	delta = now - FIRST_DAY
	return delta.days % 14,delta.days//7 + 1 

# Для любой даты
def any_date(str):
	date = list(map(int,str.split(".")))
	try:
		date = dt.date(date[2],date[1],date[0])
		if date.year >= 2023:
			return "BIG_YEAR",None
		if date < FIRST_DAY + dt.timedelta(days=3):
			return "NO_YEAR",None

		delta = date - FIRST_DAY
		return delta.days % 14,delta.days//7 + 1 
	except:
		return "UNKNOWN_DATE",None

# Для завтрашнего дня
def tomorrow_date():
	tomorrow = dt.date.today() + dt.timedelta(days=1)
	if tomorrow.year >= 2023:
		return "BIG_YEAR",None
	delta = tomorrow - FIRST_DAY
	return delta.days % 14,delta.days//7 + 1