number = int(input("Enter a number: "))

for number in range(1, number + 1):
    if number > 0:
        print("«Number is positive")
    elif number < 0:
        print("Number is negative")
    elif number == 0:
        print("«Number is equal to zero")

    if number == 7:
        print("Good bye")