word = list("бегемот")
guess_word = list("???????")
difficulty = 10

already_guessed = False

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
	global already_guessed
	is_changed = False

	for i in range(len(word)):
		if l == guess_word[i]:
			already_guessed = True
			is_changed = True
			break
		if l == word[i]:
			guess_word[i] = l
			is_changed = True
	return is_changed

def GuessLtr():
	print("Угадай букву в слове")
	l = input()

	global difficulty
	global already_guessed
	if ChangeLtr(l):
		x = len(guess_word) - guess_word.count('?')
		print("Угадано " + str(x) + " букв. Осталось угадать " + str( len(guess_word)-x ) + " букв")
		if already_guessed:
			print("Такая буква уже есть")
			already_guessed = False
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
