a1 = int(input("Введите первый елемент "))
d = int(input("Введите разность "))
n = int(input("Введите количество елементов "))

for i in range(n):
 print(a1 + i * d, end=' ')