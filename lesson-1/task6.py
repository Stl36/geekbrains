beginDistance = int(input("Сколько км спортсмен пробёжал в 1 день?\n"))
targetDistance = int(input("Сколько км спортсмен должен бробегать?\n"))
day = 1
while True:
    print(f"{day}-ый день: {'%.2f' % beginDistance}")
    if int(beginDistance) >= targetDistance:
        break
    day += 1
    beginDistance = beginDistance *2 1.1