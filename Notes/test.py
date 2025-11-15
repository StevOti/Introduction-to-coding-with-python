numbers = []

for i in range(0, 3):
    num = int(input("Enter a number: "))
    numbers.append(num)
    print(numbers)

last_num = input("Do you still want the last number in the list?(y/n) ")

if last_num == "n":
    numbers.remove(2)
    print(numbers)