# -*- coding: utf-8 -*-
"""
Задание 15.5

Создать функцию generate_description_from_cdp, которая ожидает как аргумент
имя файла, в котором находится вывод команды show cdp neighbors.

Функция должна обрабатывать вывод команды show cdp neighbors и генерировать
на основании вывода команды описание для интерфейсов.

Например, если у R1 такой вывод команды:
R1>show cdp neighbors
Capability Codes: R - Router, T - Trans Bridge, B - Source Route Bridge
                  S - Switch, H - Host, I - IGMP, r - Repeater

Device ID        Local Intrfce     Holdtme    Capability  Platform  Port ID
SW1              Eth 0/0           140          S I      WS-C3750-  Eth 0/1

Для интерфейса Eth 0/0 надо сгенерировать такое описание
description Connected to SW1 port Eth 0/1

Функция должна возвращать словарь, в котором ключи - имена интерфейсов,
а значения - команда задающая описание интерфейса:
'Eth 0/0': 'description Connected to SW1 port Eth 0/1'


Проверить работу функции на файле sh_cdp_n_sw1.txt.
"""
import re

def generate_description_from_cdp(in_file):
    regex = (r'(?P<rem_host>\S+)\s+(?P<local_intf>\S+ \d+/\d+).*\s+(?P<remote_intf>\S+ \d+/\d+)')
    template = 'description Connected to {} port {}'
    description = {}
    with open(in_file) as f_in:
        for match in re.finditer(regex, f_in.read()):
            rem_host, loc_int, rem_int = match.group('rem_host', 'local_intf', 'remote_intf')
            description[loc_int] = template.format(rem_host, rem_int)
        return description

if __name__ == "__main__":
    print(generate_description_from_cdp('sh_cdp_n_sw1.txt'))