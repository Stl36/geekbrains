a = int(input("Сколько км спортсмен пробёжал в 1 день?\n"))
b = int(input("Сколько км спортсмен должен бробегать?\n"))
day = 1
while True:
    print(f"{day}-ый день: {'%.2f' % a}")
    day += 1
    if int(a) >= b:
        break
    a = a * 1.1