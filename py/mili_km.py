def ml_calc():
    result_mil = input('Введите колличество миль')
    return 1.609 * int(result_mil)
result = ml_calc()
print(str(result) + ' meters')