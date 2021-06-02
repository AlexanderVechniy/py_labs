from tkinter import Tk, Canvas
from datetime import datetime, date

root = Tk()
canvas = Canvas(root, width = 800, height = 600, bg='yellow')
canvas.pack()
canvas.create_text(100, 50, anchor='w', fill='black', font='Timesnewroman 20 bold underline',
				   text = "Первое приложение. \nКалендарь ожидания.")

vertical_space = 100

events_file = open("events.txt")
data = events_file.read().split(sep = '\n')
print("DATA:", data)
for i in range(len(data)):
	data[i] = data[i].split(sep = ',')
del data[len(data) - 1]
print("DATA:", data)
def get_weekday(day):
	if day == 0:
		return "понедельник"
	elif day == 1:
		return "вторник"
	elif day == 2:
		return "среда"
	elif day == 3:
		return "четверг"
	elif day == 4:
		return "пятница"
	elif day == 5:
		return "суббота"
	elif day == 6:
		return "воскресенье"

def get_day_type(day):
	if 0 <= day <= 4:
		return "будний день"
	elif day == 5 or day == 6:
		return "выходной"

def days_till_deadline(data):
	today = datetime.today()
	date = datetime.strptime(data[1], "%d/%m/%Y")
	days_remain = (date - today).days
	day_type = get_day_type(date.weekday())
	weekday = get_weekday(date.weekday())

	if days_remain > 0:
		output = "До праздника " + str(data[0]) + " осталось " + str(days_remain) + " дней.\n"
		output += "Это будет " + day_type + " " + weekday + "."
	else:
		output = "Праздник " + str(data[0]) + " уже прошел " + str(-days_remain) + " дней назад.\n"
		output += "Это был " + day_type + " " + weekday + "."

	return output


vertical_space = 120

for i in range(len(data)):
	display = days_till_deadline(data[i])
	canvas.create_text(50, vertical_space, anchor='w', fill='blue', font='Arial 15 bold', text=display)
	vertical_space += 50

root.mainloop()

events_file.close()
