""" Имеется набор чисел. Выведите УГАДАЛ если вол число из этого списка. """

A = int(input("Ведите число чтобы угадать:"))
S = [0, 1, 2, 3]
if A in S:
    print("Bingo")
    print("Exit")
