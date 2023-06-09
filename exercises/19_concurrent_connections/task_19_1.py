# -*- coding: utf-8 -*-
"""
Задание 19.1

Создать функцию ping_ip_addresses, которая проверяет пингуются ли IP-адреса.
Проверка IP-адресов должна выполняться параллельно в разных потоках.

Параметры функции ping_ip_addresses:
* ip_list - список IP-адресов
* limit - максимальное количество параллельных потоков (по умолчанию 3)

Функция должна возвращать кортеж с двумя списками:
* список доступных IP-адресов
* список недоступных IP-адресов

Для выполнения задания можно создавать любые дополнительные функции.

Для проверки доступности IP-адреса, используйте ping.

Подсказка о работе с concurrent.futures:
Если необходимо пинговать несколько IP-адресов в разных потоках,
надо создать функцию, которая будет пинговать один IP-адрес,
а затем запустить эту функцию в разных потоках для разных
IP-адресов с помощью concurrent.futures (это надо сделать в функции ping_ip_addresses).
"""

import subprocess
from concurrent.futures import ThreadPoolExecutor

def ping_single(host):
    reply = subprocess.run(['ping', '-n', '5', host], stdout=subprocess.DEVNULL)
    if reply.returncode == 0:
        return True
    else:
        return False


def ping_ip_addresses(ip_list, limit=3):
    with ThreadPoolExecutor(max_workers=limit) as executor:
        ok_list = []
        fail_list = []
        result = executor.map(ping_single, ip_list)
        for ip, output in zip(ip_list, result):
            if output:
                ok_list.append(ip)
            else:
                fail_list.append(ip)
        return ok_list, fail_list

if __name__ == "__main__":
    ip_test_list = ['8.8.8.8', '192.168.100.150', '127.0.0.1', '192.168.100.111', '192.168.100.1', '192.168.100.123']
    print(ping_ip_addresses(ip_test_list, 6))