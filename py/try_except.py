while True:
    try:
        x = float(input("Please enter a first number: "))
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")
        break

    try:
        y = float(input("Please enter a second number: "))
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")
        break

    try:
        division = float(x / y)
        print("The quotient of your numbers: " + str(division))
        break
    except ZeroDivisionError:
        print("It is not necessary to divide by zero xD")
        break