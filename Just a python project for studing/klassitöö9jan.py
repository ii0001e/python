from klassitöö9jan_mod import *
from operator import *
#################################################
# (1)
# Простейшие арифметические операции 
# Написать функцию arithmetic, принимающую 3 аргумента: первые 2 - числа, третий - операция,
# которая должна быть произведена над ними. 
# Если третий аргумент +, сложить их; если —, то вычесть; * — умножить; / — разделить (первое на второе). 
# В остальных случаях вернуть строку "Неизвестная операция".
#################################################

a = arithmetic(2.5,1.8,"+")
print(a)
#a = arithmetic(input(),input(),input())
#print(a)

#################################################
# (2)
# Високосный год 
# Написать функцию is_year_leap, принимающую 1 аргумент — год, и возвращающую True, если год високосный, 
# и False иначе.
#################################################
b = is_year_leap(2022)
print(b)

#################################################
# (3)
# Квадрат 
# Написать функцию square, принимающую 1 аргумент — сторону квадрата, и возвращающую 3 значения: 
# периметр квадрата, площадь квадрата и диагональ квадрата.
#################################################

a = square(5)
print(a)
#################################################
# (4)
# Времена года 
# Написать функцию season, принимающую 1 аргумент — номер месяца (от 1 до 12), и возвращающую время года, 
# которому этот месяц принадлежит (talv, kevad, suvi или sügis).
#################################################
a = season(10)
print(a)

#################################################
# (5)
# Банковский вклад 
# Пользователь делает вклад в размере a евро сроком на years лет под 10% годовых 
# (каждый год размер его вклада увеличивается на 10%. Эти деньги прибавляются к сумме вклада, 
# и на них в следующем году тоже будут проценты).
# Написать функцию bank, принимающая аргументы a и years, и возвращающую сумму, 
# которая будет на счету пользователя.
#################################################
a = bank(10,400)
print(a)
#################################################
# (6)
# Простые числа 
# Написать функцию is_prime, принимающую 1 аргумент — число от 0 до 1000, и возвращающую True, 
# если оно простое, и False - иначе.
#################################################
print("is_prime")
a = is_prime(6)
print (a)
#################################################
# (7)
# Правильная дата 
# Написать функцию date, принимающую 3 аргумента — день, месяц и год. 
# Вернуть True, если такая дата есть в нашем календаре, и False иначе.
#################################################
a = date(22,11,22)
print (a)
#################################################
# (8)
# XOR-шифрование 
# Написать функцию XOR_cipher, принимающая 2 аргумента: строку, которую нужно зашифровать, 
# и ключ шифрования, которая возвращает строку, зашифрованную путем применения функции XOR (^) 
# над символами строки с ключом. Написать также функцию XOR_uncipher, которая по зашифрованной строке
# и ключу восстанавливает исходную строку.
#################################################

XOR_code("Hello!",123)
XOR_decode(XOR_code("Hello!",123),12345)

