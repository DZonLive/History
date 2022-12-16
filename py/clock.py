n = int(input("Количество минут после 00:00: "))
hours = n//60%24
mins = n%60
list = [mins]
for minut in list:
    if minut < 10:
        0 + minut
print(f"{hours}:{minut}")