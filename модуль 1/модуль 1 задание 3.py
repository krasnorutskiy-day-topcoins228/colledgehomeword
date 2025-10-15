meter_to_miles=0.000621371
meter_to_inches=39.3701
meter_to_yeards=1.09361

meters=float(input("Введите количество метров:"))
print('Выберите единицы,в которую нужно перенсти')
print('1 - Мили')
print('2 - Дюймы')
print('3 - Ярды')

choice=input("Ваш выбор:")

if choice=="1":
    print(f"{meters}метров={meters*meter_to_miles}миль")
elif choice=="2":
    print(f"{meters}метров={meters*meter_to_inches}Дюймы")
elif choice=="3":
    print(f"{meters}метров={meters*meter_to_yeards}Ярды")
else:
    print("Ошибка:неизвестный выбор.")