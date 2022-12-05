#1- Задайте список из нескольких чисел. 
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
#Пример:
#[2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# def sum_odd_index(lst):
#     s = 0
#     for i in range(1, len(lst), 2):
#         # if i % 2 != 0:
#         s += lst[i]
#     print(f"Сумма равна: {s}")

# lst = [2, 3, 5, 9, 3]
# sum_odd_index(lst)


# Решение на семинаре

import random
from typing import List
def create_list(numbs = []):
    for i in range(int(input('Введите количество элементов списка: '))):
        numbs.append(random.randint(1,9))
    return numbs

def get_sum_odd_elements(numbers: List[int]) -> int:
    s = 0
    for n in range(1, len(numbers), 2):
        s += n
    return s

numbers = create_list()
print(f'исходный список {numbers}')
print(f'сумма элементов на нечетных позициях = {get_sum_odd_elements(numbers)}')
