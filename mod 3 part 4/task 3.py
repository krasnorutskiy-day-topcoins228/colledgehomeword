number1 = int(input())
number2 = int(input())
for i in range(number1, number2 + 1):
    for j in range(number1, number2 + 1):
        print(f"{i} x {j} = {i * j}")
print()