# В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
# В случае с английским алфавитом очки распределяются так:
# A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка;
# B, C, M, P – 3 очка;
# F, H, V, W, Y – 4 очка;
# K – 5 очков; J,
# X – 8 очков;
# Q, Z – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит  только английские буквы.

a = input('insert the word: ')
b = list()
summ = 0
for i in range(len(a)):
    if a[i] == 'd' or a[i] == 'g':
        b.insert(i,2)
    elif a[i] == 'b' or a[i] == 'c' or a[i] == 'm' or a[i] == 'p':
        b.insert(i,3)
    elif a[i] == 'f' or a[i] == 'h' or a[i] == 'v' or a[i] == 'w' or a[i] == 'y':
        b.insert(i,4)
    elif a[i] == 'k':
        b.insert(i,5)
    elif a[i] == 'j' or a[i] == 'x':
        b.insert(i,8)
    elif a[i] == 'q' or a[i] == 'z':
        b.insert(i,10)
    else:
        b.insert(i,1)
for i in range(len(a)):
    summ += b[i]
print(summ)
