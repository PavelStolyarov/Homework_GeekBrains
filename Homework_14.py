# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

n = int(input("Enter number: "))
flag = True

answer = 1

power = 0

while flag:
    print(answer, end=" ")
    power += 1
    answer = 2 ** power 
    flag = answer <= n