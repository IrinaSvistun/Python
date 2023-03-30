# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

m = int(input("введите m: "))
n = int(input("введите n: "))
k = int (input("введите k: "))
if n%k==0 or m%k==0 and k < m*n:
    print ("Yes")
else: print ("No")


# m = int(input("введите m: "))
# n = int(input("введите n: "))
# k = int (input("введите k: "))
# z = 0
# i = 1
# if m > n:
#     temporary = m
#     m=n
#     n = temporary
# while i< n:
#     if i*m ==k:
#         z = 1
#     i+=1
# if z>0:
#     print ("Yes")
# else: print ("No")

