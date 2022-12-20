# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

n = int(input("Введите число: "))
from random import randint

list = []
for i in range(n):
    list.append(randint(-n, n))
print(list)

with open ('file.txt', 'a') as data:
    data.write('0\n')
    data.write('2\n')
mult = 1
path = 'file.txt'
data = open(path, 'r')
for line in data:
    mult *= list[int(line)]
print(mult)
data.close()
