# -*- coding: utf-8 -*-
"""
Задание 7.2b

Переделать скрипт из задания 7.2a: вместо вывода на стандартный поток вывода,
скрипт должен записать полученные строки в файл

Имена файлов нужно передавать как аргументы скрипту:
 * имя исходного файла конфигурации
 * имя итогового файла конфигурации

При этом, должны быть отфильтрованы строки, которые содержатся в списке ignore
и строки, которые начинаются на '!'.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
from sys import argv

ignore = ["duplex", "alias", "configuration"]

with open(argv[1], 'r') as f, open(argv[2], 'w') as dest:
    for line in f:
        good_line = True
        if not line.startswith('!'):
            for i in ignore:
                if line.count(i):
                    good_line = False
            if good_line:
                dest.write(line)