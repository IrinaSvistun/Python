# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

x = int(input('input number of items in list: '))
list_1 = list()
count = 0
for i in range(x):
    print('input ', (i+1), 'item:')
    list_1.append(int(input()))
print (list_1)
n = int(input('input number for search: '))
for i in range(x):
    if list_1[i] == n:
        count += 1
print('result: ', count, ' items ', n, 'in list')
