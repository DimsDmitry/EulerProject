#Если выписать все натуральные числа меньше 10, кратные 4 или 9, то получим 4,8,9.
# Сумма этих чисел равна 21.
#Найдите сумму всех чисел меньше 1000, кратных 4 или 9.

summa = 0
a = 1
for i in range(999):
    if a % 3 == 0 or a % 5 == 0:
        summa += a
    a += 1
print('Сумма всех чисел меньше 1000, кратных 3 или 5:', summa)
