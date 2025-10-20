count=0
for number in range(100,999+1):
    number_str=str(number)
    if (number_str[0]==number_str[1] or number_str[0]==number_str[2] or number_str[1]==number_str[2]):
        count += 1
    print(count)

