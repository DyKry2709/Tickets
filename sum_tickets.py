sum_tick = 0
quan_tick = int(input('Введите количество билетов: '))

for i in range(quan_tick):
    age = int(input('Введите возраст посетителя №{}: '.format(i + 1)))
    if age < 18:
        sum_tick = 0
    elif 18 <= age <= 25:
        sum_tick += 990
    else:
        sum_tick += 1390
    if quan_tick > 3:
        sum_tick = round(sum_tick * 0.9)
    if sum_tick < 0:
        print(0)

print('Стоимость ваших билетов: ', sum_tick)

