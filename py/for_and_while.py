                    #for
my_list = [7, 5, 4, 4, 3, 2, 1, -1, -2, -5, -6, -9]
sum = 0
for element in my_list:
    if element <= 0:
        sum += element
print(sum)
                    #while
totalsum = 0
t = -1
while my_list[t] < 0:
    totalsum += my_list[t]
    t -= 1
print(totalsum)

list1 = ["hello", "hi", "good", "stop", "jump"]
for note in list1:
    if note == "stop":
        break
    print(note, end=" ")
