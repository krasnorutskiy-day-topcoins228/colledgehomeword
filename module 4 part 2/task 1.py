expression=input("Введите арифметическое выражение: ").strip()
num1,operator,num2=expression.split()
num1=float(num1)
num2=float(num2)
if operator=="+":
    print(num1+num2)
elif operator=="-":
    print(num1-num2)
elif operator=="*":
    print(num1*num2)
elif operator=="/":
    if num2==0:
        print("Ошибка деления на ноль!")
else:
    result=num1 / num2
    print("Ошибка: неверная операция!")
    if 'result' in locals():
        print(f'Результат: {result:.2f}')


