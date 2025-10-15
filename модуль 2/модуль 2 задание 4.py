print("Введите числа:")
num1=int(input())
num2=int(input())

if num1==num2:
    print("Числа равны")
else:
    num_list=[num1,num2]
    (num_list.sort())
    print(num_list)