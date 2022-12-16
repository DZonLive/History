number1 = input("Введите первое число")
number2 = input("Введите дополнительное число")
def my_function(n,k):
    if n>20:
        print("Больше 20")
        return(0)
    else:
        total_sum = 0
        for sum in range(1,n + 1):
            if sum % 2 == 0:
                total_sum = total_sum + sum**k
        return (total_sum)
art = my_function(int(number1),int(number2))
print(art)


