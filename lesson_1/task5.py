revenue = int(input("Введите прибыль фирмы\n"))
costs = int(input("Введите издержки фирмы\n"))
def toFixed(numObj, digits=0):
    return f"{numObj:.{digits}f}"
if revenue < costs:
    print("Фирма работает в убыток")
elif revenue == costs:
    print("Фирма выходит в '0'")
else:
    profitability = ((revenue - costs) / revenue * 100)
    print(f"Фирма работает в прибыль\n"
          f"Рентабельность {toFixed(profitability, 2)}%"
          )
    staf = int(input("Введите число сотрудников в фирме "))
    print(f"Прибыль фирмы в расчете на одного сотрудника {toFixed((revenue - costs) / staf, 2)} национальных рублей")