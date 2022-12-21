# Реализуйте алгоритм перемешивания списка.

from random import randint, shuffle
list = []
for i in range(5):
    list.append(randint(-10, 10))
print(list)

shuffle(list)
print(list)
