abc = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдежзийклмнопрстуфхцчшщъыьэюя"

def Codelist(text, abc):
	codelist = []
	for c in text:
		if c in abc:
			codelist.append(abc.find(c))
		else:
			codelist.append(-1)
	return codelist

def Encrypt(text, abc, shift):
	output = list(text)
	codelist = Codelist(text, abc)
	for i in range(len(codelist)):
		if codelist[i] == -1:
			continue
		if abc[codelist[i]] in abc[0:32]:
			codelist[i] = ( codelist[i] + shift ) % 32
		elif abc[codelist[i]] in abc[32:64]:
			codelist[i] = 32 + ( (codelist[i] + shift ) % 32)
	
	for i in range (len(output)):
		if codelist[i] != -1:
			output[i] = abc[codelist[i]]
	return ''.join(output)
	

def TheProgram():
	text = list(input("Введите текст "))
	length = len(text)
	select_option = int(input("Зашифровать(1) или расшифровать(2)? Введите 1 или 2 "))
	shift = int(input("Введите сдвиг "))
	if select_option == 1:
		print("Результат: ", Encrypt(text, abc, shift))
	elif select_option == 2:
		print("Результат: ", Encrypt(text, abc, -shift))
	else:
		print("Вывод не распознан")

if __name__=='__main__':
	TheProgram()
	a = input()