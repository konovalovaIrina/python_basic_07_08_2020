"""Урок 1. Задача 2.
2. Пользователь вводит время в секундах.
Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.
"""
sec = int(input('Введите секунды: '))
h = ((sec // 3600)) % 24
m = (sec // 60) % 60
s = sec % 60

print('%d:%02d:%02d' % (h, m, s))
# OR
print('{0}:{1:=02}:{2:=02}'.format(h, m, s))
