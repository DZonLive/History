result = input("Введите любое число")
for proc in result:
    if int(proc) % 2 == 0:
        print("Ваше число является четным")
    else:
        print("Ваше число является нечетным")