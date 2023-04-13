# Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

def power(a, b, sum = 1):
    if b == 0:
        return sum
    return power(a, b-1, sum*a)
    

a = int(input('input A (number): '))
b = int(input('input b (power): '))
print (power (a,b))

