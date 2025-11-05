sum = 0
maxi = 0
mini = 0
count = 0
total_sum = 0
while True:
    number = int(input())
    total_sum += number
    if number > maxi:
        maxi = number
    elif number < mini:
        mini = number

    if number == 7:
        print("Good bye!")
        break

    print(total_sum)
    print(maxi)
    print(mini)