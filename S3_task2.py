# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

x = int(input('input number of items in list: '))
list_1 = list()
for i in range(x):
    print('input ', (i+1), 'item:')
    list_1.append(int(input()))
print(list_1)
n = int(input('input number for search: '))
nearest_item = list_1[0]
min_difference = abs(list_1[0] - n)
for i in range(x):
    if abs(list_1[i] - n) < min_difference:
        min_difference = abs(list_1[i] - n)
for i in range(x):
    if abs(list_1[i] - n) == min_difference:
        print('nearest item: ', list_1[i], 'position ', i)
