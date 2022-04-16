print('1. Печать строки N раз')
print('Этот пример может печатать любую строку n раз без использования циклов Python.')

n = 5
string = "Hello World "
print(string * n)  # Hello World Hello World Hello World Hello World Hello World

print('2. Объединяем два словаря')
print('Этот пример выполняет слияние двух словарей в один.')

def merge(dic1, dic2):
    dic3 = dic1.copy()
    dic3.update(dic2)
    return dic3

dic1 = {1 : "hello", 2 : "world"}
dic2 = {3 : "Python", 4 : "Programming"}
print( merge(dic1, dic2) )# {1: 'hello', 2: 'world', 3: 'Python', 4: 'Programming'}

print('3. Вычисляем время выполнения')
print('Этот пример полезен, когда вам нужно знать, сколько времени требуется для выполнения программы или функции.')

def fun():
    a=0
    for i in range (1000000):
        a+=1
    print(a)

from time import time
start_time = time()
fun()
end_time = time()
timetaken = end_time - start_time
print("Your program takes: ", timetaken) # 0.05

print('4. Обмен значений между переменными')
print('Это быстрый способ обменять местами две переменные без использования третьей.')

a = 3
b = 4
print(a, b) # a = 3, b = 4
print("меняем местами значения переменных")
a, b = b, a
print(a, b) # a = 4, b = 3

print('5. Проверка дубликатов')
print('Это самый быстрый способ проверки наличия повторяющихся значений в списке.')

def check_duplicate(lst):
    return len(lst) != len(set(lst))

print('[1,2,3,4,5,4,6] ', check_duplicate([1,2,3,4,5,4,6])) # True
print('[1,2,3] ', check_duplicate([1,2,3])) # False
print('[1,2,3,4,9] ', check_duplicate([1,2,3,4,9])) # False

print('6. Фильтрация значений False')
print('Этот пример используется для устранения всех ложных значений из списка, например false, 0, None, "".')

def Filtering(lst):
    return list(filter(None,lst))
lst=[None,1,3,0,"",5,7]
print(lst, Filtering(lst)) #[1, 3, 5, 7]

print('7. Размер в байтах')
print('Этот пример возвращает длину строки в байтах, что удобно, когда вам нужно знать размер строковой переменной.')

def ByteSize(string):
    return len(string.encode("utf8"))
print('"Python": ', ByteSize("Python")) #6
print('"Data": ', ByteSize("Data")) #4
print('"Слово:" ', ByteSize("Слово"))

print('8. Занятая память')
print('Пример позволяет получить объём памяти, используемой любой переменной в Python.')

from sys import getsizeof
var1="Python"
var2=100
var3=True
print('"Python": ', getsizeof(var1)) #55
print('100: ', getsizeof(var2)) #28
print('True: ', getsizeof(var3)) #28

print('9. Анаграммы')
print('Этот код полезен для проверки того, является ли строка анаграммой. Анаграмма — это слово, полученное перестановкой букв другого слова.')

from collections import Counter
def anagrams(str1, str2):
    return Counter(str1) == Counter(str2)
print('"abc1","1bac"', anagrams("abc1", "1bac")) # True

print('10. Сортировка списка')
print('Этот пример сортирует список. Сортировка — это часто используемая задача, которую можно реализовать множеством строк кода с циклом, но можно ускорить свою работу при помощи встроенного метода сортировки.')

my_list =  ["leaf", "cherry", "fish"]
my_list1 = ["D","C","B","A"]
my_list2 = [1,2,3,4,5]

print('["leaf", "cherry", "fish"]', '=>', sorted(my_list)) # ['cherry', 'fish', 'leaf']
print('["D","C","B","A"]', '=>', sorted(my_list1)) # ['A', 'B', 'C', 'D']
print('[1,2,3,4,5]', '=>', sorted(my_list2, reverse=True)) # [5, 4, 3, 2, 1]

print('11. Сортировка словаря')
print('''orders = {
'pizza': 200,
'burger': 56,
'pepsi': 25,
'coffee': 14
}''')
orders = {
'pizza': 200,
'burger': 56,
'pepsi': 25,
'coffee': 14
}
sorted_dic = sorted(orders.items(), key=lambda x: x[1])
print('sorted_dic = ', sorted_dic)  # [('coffee', 14), ('pepsi', 25), ('burger', 56), ('pizza', 200)]


print('14. Получение последнего элемента списка')

my_list = ["Python", "JavaScript", "C++", "Java", "C#", "Dart"]
print("mylist[-1] возвращает", my_list[-1])  # Dart
print("mylist.pop() возвращает", my_list.pop()) # Dart

print('15. Преобразование разделённого запятыми списка в строку')
print('Этот код преобразует разделённый запятыми список в единую строку. Его удобно использовать, когда нужно объединить весь список со строкой.')

my_list1=["Python","C","C++"]
my_list2=["C#", "JavaScript"]
print('''my_list1=["Python","JavaScript","C++"]
my_list2=["Java", "Flutter", "Swift"]''')
#example 1
print("Мои любимые языки программирования:", ", ".join(my_list1), ", ".join(my_list2)) # My favourite Programming Languages are Python, JavaScript, C++