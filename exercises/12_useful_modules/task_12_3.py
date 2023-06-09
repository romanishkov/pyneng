# -*- coding: utf-8 -*-
"""
Задание 12.3

Создать функцию print_ip_table, которая отображает таблицу доступных
и недоступных IP-адресов.

Функция ожидает как аргументы два списка:
* список доступных IP-адресов
* список недоступных IP-адресов

Результат работы функции - вывод на стандартный поток вывода таблицы вида:

Reachable    Unreachable
-----------  -------------
10.1.1.1     10.1.1.7
10.1.1.2     10.1.1.8
             10.1.1.9

"""

from tabulate import tabulate
from task_12_1 import ping_ip_addresses

def print_ip_table(ok_list, fail_list):
    result_dict = {"Reachable": ok_list, "Unreachable": fail_list}
    print(tabulate(result_dict, headers="keys"))
    
if __name__ == "__main__":
    test_list = ['127.0.0.1', '172.16.1.1', '8.8.8.8', '10.0.143.5']
    ok, fail = ping_ip_addresses(test_list)
    print_ip_table(ok, fail)