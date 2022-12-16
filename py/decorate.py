def decorate(funct):
	def wrapper(value):
		print('wrapper')
		funct(value)
	return wrapper

@decorate
def test(value):
	print(f"test, value: {value}")

test('value in test')

#####################################################################################

def decorate(func):
    def wrapper():
        print (1)
        func()
        print(2)
    return wrapper

def decorate2(func):
    def wrapper():
        print (1)
        func()
        print(2)
    return wrapper

@decorate
@decorate2

def show():
    print("Середина")

show()