# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# # Вам требуется написать программу, которая проверяет счастливость билета.

# *Пример:*

# 385916 -> yes
# 123456 -> no
#Решение:
a = int(input("введите шестизначное число : "))
b=a//100000
c=a//10000
c=c%10
d=a//1000
d=d%10
e=a//100
e=e%10
f=a//10
f=f%10
g=a%10
if b+c+d==e+f+g :
    print("yes")
else:
    print("no")
