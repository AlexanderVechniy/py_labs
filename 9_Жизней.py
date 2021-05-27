word = list("бегемот")
guess_word = list("???????")
difficulty = 10

# Легкая сложность = 9 жизней
def ChooseDifficulty():
	print("Выберите сложность (1, 2 или 3):")
	print("1 Легкий")
	print("2 Средний")
	print("3 Сложный")
	global difficulty
	difficulty = 10
	difficulty -= int(input())

def PrintMsg():
	global guess_word
	print(guess_word)
	for i in range (difficulty):
		print('❤️', end='')
	print()

def ChangeLtr(l):
	global word
	global guess_word

	is_changed = False

	for i in range(len(word)):
		if l == word[i]:
			guess_word[i] = l
			is_changed = True
	return is_changed

def GuessLtr():
	print("Угадай букву в слове")
	l = input()

	global difficulty
	if ChangeLtr(l):
		x = len(guess_word) - guess_word.count('?')
		print("Угадано " + str(x) + " букв. Осталось угадать " + str( len(guess_word)-x ) + " букв")
		if guess_word.count(l) > 0:
			print("Такая буква уже есть")
	else:
		print("Такой буквы здесь нет =( Попробуйте еще раз")
		difficulty -= 1

def IsOver():
	if guess_word.count('?') == 0:
		return True
	if difficulty == 0:
		return True
	return False

def ResetGame():
	global word
	global guess_word
	global difficulty
	if difficulty == 0:
		print("Вы проиграли=(")
		print("Загаданое слово " + ''.join(word))
	else:
		print("Ура, вы отгадали слово!")
	print("Сыграем еще раз? Да/Нет")
	if input() == "Да":
		word = list("бегемот")
		guess_word = list("???????")
		difficulty = 10
		TheGame()
	else:
		return

def TheGame():
	ChooseDifficulty()
	while not IsOver():
		PrintMsg()
		GuessLtr()
	ResetGame()

TheGame()