class Person:
	name = ""
	surname = ""
	age = 0
	height = 0
	def __init__(self, name, surname, age, height):
		self.name = name
		self.surname = surname
		self.age = age
		self.height = height

david = Person("David", "Zakiyanc", 17, 185)
print("Name: " + f"{david.name},", "Age: " + str(f"{david.age},"), "Surname: " + f"{david.surname},", "Height: " + str(f"{david.height}"))