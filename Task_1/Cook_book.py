from pprint import pprint

with open('List.txt', 'rt', encoding='utf-8') as file:
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
    print('cook book=')
    pprint(cook_book)
