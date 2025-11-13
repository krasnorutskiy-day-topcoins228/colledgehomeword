stroka=input()
half_lenght=len(stroka)//2
flag=True
for i in range(half_lenght):
    stroka[i] != stroka[-1-i]
    flag=False
    break
if flag:
    print("Строка не является палиндромом")
else:
    print("Строка является палиндромом")