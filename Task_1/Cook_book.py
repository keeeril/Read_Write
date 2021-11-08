import os
from pprint import pprint
path = os.path.join(os.getcwd(), 'Task_1/List.txt')
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
# pprint(cb())


def get_shop_list_by_dishes(dishes, person_count):
    list_products = {}
    for dish in dishes:
        for i in cb()[dish]:
            count_measure = {'measure': i['measure'], 'count': (int(i['count'])*person_count)}
            list_products[i['product']] = count_measure
    pprint(list_products)

get_shop_list_by_dishes(['Омлет', 'Омлет'], 1)


def get_shop_list_by_dishes(dishes, person_count):
    list_products = {}
    for dish in dishes:
        for i in cb()[dish]:
            products = [i['product']]
            count_measure = {'measure': i['measure'], 'count': (int(i['count'])*person_count)}
            list_products[i['product']] = count_measure
    # pprint(list_products)

get_shop_list_by_dishes(['Омлет', 'Омлет', 'Запеченный картофель'], 1)
