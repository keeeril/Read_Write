import os
# path = os.path.join(os.getcwd())
import glob
def do_new_file():
    data = {}
    for path in glob.glob('*txt'):
        with open(path, 'rt', encoding='utf-8') as file:
            count_line = len(file.readlines())
        with open(path, 'rt', encoding='utf-8') as file:
            data[path] = [count_line, file.read().strip()]
    with open('new.txt', 'a', encoding='utf-8') as new_file:
        data = sorted(data.items(), key=lambda x: x[1])
        for i in data:
            new_file.write(i[0] + '\n')
            for j in i[1]:
                new_file.write(str(j) + '\n')
do_new_file()
