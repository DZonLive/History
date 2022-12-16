try:
	with open('text.txt', 'wt', encoding='utf-8') as inFile:
		num = int(input())
		result = str('1 / ' + str(num) + ' = ' + str(1 / num))
		print(result)
		inFile.write(result)
except ValueError:
    num = 0
    print('Вы ввели текст.')