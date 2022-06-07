print("*" * 20 + " Задание 1 " + "*" * 20)
q = input()
print(type(q))


print('*')
print('*')
print("*" * 20 + " Задание 2 " + "*" * 20)
sec = int(input('введите секунды: '))
h = sec / 3600
h = int(h)
m = (sec - (h * 3600)) / 60
m = int(m)
s = sec % 60
print(f'{h}:{m}:{s}')
sec = s + (m * 60) + (h * 3600)
print('проверка', sec)


print('*')
print('*')
print("*" * 20 + " Задание 3 " + "*" * 20)

n = input('введите число: ')
n1 = int(n)
n2 = int(n + n)
n3 = int(n + n + n)
print(n+' + '+n+n+' + '+n+n+n+' =', n1 + n2 + n3)


print('*')
print('*')
print("*" * 20 + " Задание 4 " + "*" * 20)

n = int(input('введите число: '))
n1 = n % 10
while n >= 1:
    n = n // 10
    if n % 10 > n1:
        n1 = n % 10
    if n > 9:
        continue
    else:
        print("Максимальное число: ", n1)
        break

print('*')
print('*')
print("*" * 20 + " Задание 5 " + "*" * 20)


vir = int(input("Введите выручку: "))
izd = int(input("Введите издержки: "))
if vir > izd:
    print("прибыль — выручка больше издержек")
else:
    print('убыток — издержки больше выручки')

print('*')
print('*')
print("*" * 20 + " Задание 6 " + "*" * 20)

print("Рентабельность: ", int((vir - izd) / vir * 100), '%')
chel = int(input('Сколько численность сотрудников фирмы: '))
print('Прибыль фирмы в расчёте на одного сотрудника: ', (vir - izd) / chel)


print('*')
print('*')
print("*" * 20 + " Задание 7 " + "*" * 20)




a = int(input('Введите результат первого дня в км: '))
b = int(input("Какой результат хотите достичь в км: "))
num_day = 1
print(num_day, '-day: ', a, 'km')
while a < b:
    num_day = num_day + 1
    a = a * 1.1
    a = round(a, 2)
    print(num_day, '-day: ', a, 'km')
print('на', num_day, 'день спортсмен достиг результата не', b, 'km')


print('ДЗ 1-урок ВЫПОЛНЕНО.')