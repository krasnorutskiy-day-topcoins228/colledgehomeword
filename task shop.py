products = {
    "Фрукты:": [("Яблоки —", 15, 60), ("Бананы —", 10, 80), ("Манго —",7,100)],
    "Овощи:": [("Морковь —", 20, 30), ("Огурец —",30,50)]
}
max_price = 0

for key in products:
    print(key)
    for product in products[key]:
        name,quantity,price = product
        print(f"{name} {quantity} шт.,{price} руб.")
        if price > max_price:
            max_price = price


def find_category_with_most_items(products):
    max_quantity = 0

    for category,items in products.items():
        total_quantity = sum(item[1] for item in items)
        if total_quantity > max_quantity:
            max_quantity = total_quantity
        return max_quantity
max_quantity = find_category_with_most_items(products)


def calculate_total_value(products):
    total_value = 0

    for category, items in products.items():
        for item in items:
            total_value += item[1] * item[2]

    return total_value
total_value = calculate_total_value(products)
print(f"\nКатегория в которой больше всего товаров: {max_quantity} шт.")
print('Самая большая цена на продукт:',max_price)
print(f"Общая стоимость всех товаров: {total_value} руб.")

