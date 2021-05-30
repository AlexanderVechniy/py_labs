abc = "АБВГДЕЖЗИКЛМНОПРСТФХЦЧШЩЪЫЬЭЮЯабвгдежзиклмнопрстфхцчшщъыьэюя"

def Encrypt(text):

 return

def Decrypt(text):

 return

def TheProgram():
	print("Введите текст")
	text = list(input())
	length = len(text)
	print("Зашифровать(1) или расшифровать(2)? Введите 1 или 2")
	select_option = int(input())

	if select_option == 1:
		print(Encrypt(text))
	elif select_option == 2:
		print(Decrypt(text))
	else:
		print("Вывод не распознан")

 if __name__=='__main__':
	TheProgram()