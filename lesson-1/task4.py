number = int(input("Введите число\n"))
k = number % 10
x = number // 10
while x != 0:
    if k < (x % 10):
        k = x % 10
    x = x // 10
print(f"Самая большая цифра в числе {k}")