import os
import glob
from pprint import pprint
path = os.path.join(os.getcwd(), 'Task_1/List.txt')
print('Задача 1')
def cb():
    with open(path, 'rt', encoding='utf-8') as file:
        cook_book = {}
        for dish in file:
            name_dish = dish.strip()
            count_products = int(file.readline().strip())
            list_products = []
            for items in range(count_products):
                product, count, measure = file.readline().split('|')
                new_list = {'product': product.strip(), 'count': count.strip(), 'measure': measure.strip()}
                list_products.append(new_list)
            cook_book[name_dish] = list_products
            file.readline()
        return cook_book
pprint(cb())


print()
print('Задача 2')
def get_shop_list_by_dishes(dishes, person_count):
    list_products = {}
    dishes_quantity = {}
    for prod in list(set(dishes)):
        dishes_quantity[prod] = 0

    for dish in dishes:
        dishes_quantity[dish] +=1

    # print(dishes_quantity)

    for dish in dishes:
        # print(dish)
        for i in cb()[dish]:
            # print(i)
            count_measure = {'measure': i['measure'], 'count': (int(i['count'])*person_count\
                                                                *dishes_quantity[dish])}
            list_products[i['product']] = count_measure

    return list_products

pprint(get_shop_list_by_dishes(['Омлет', 'Омлет', 'Запеченный картофель'], 2))
