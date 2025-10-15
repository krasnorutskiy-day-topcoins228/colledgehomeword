a=int(input())
b=int(input())
c=int(input())
print("Выберите операцию")
choice=input("Введите номер операции (1/2/3:")
if choice=="1":
        print("Выводит максимум из трех чисел",max(a,b,c))
elif choice=="2":
        print("Выводит минимум из трех чисел",min(a,b,c))
elif choice=="3":
        print("Выводит среднее арифметическое трех чисел",(a+b+c/2))
else:
        print("Ошибка ввода операции")