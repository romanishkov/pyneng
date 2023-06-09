# -*- coding: utf-8 -*-
"""
Задание 9.3a

Сделать копию функции get_int_vlan_map из задания 9.3.

Дополнить функцию: добавить поддержку конфигурации, когда настройка access-порта
выглядит так:
    interface FastEthernet0/20
        switchport mode access
        duplex auto

То есть, порт находится в VLAN 1

В таком случае, в словарь портов должна добавляться информация, что порт в VLAN 1
Пример словаря:
    {'FastEthernet0/12': 10,
     'FastEthernet0/14': 11,
     'FastEthernet0/20': 1 }

У функции должен быть один параметр config_filename, который ожидает
как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw2.txt

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
def get_int_vlan_map(config_filename):
    access_dict = {}
    trunk_dict = {}
    with open(config_filename) as f:
        for line in f:
            if line.lstrip().startswith("interface"):
                intf = line.split()[-1]
            if line.lstrip().startswith("switchport mode access"):
                access_dict[intf] = 1
            if line.lstrip().startswith("switchport access vlan"):
                vlan = int(line.split()[-1])
                access_dict[intf] = vlan
            if line.lstrip().startswith("switchport trunk allowed vlan"):
                vlan = [int(vl) for vl in line.split()[-1].split(',')]
                trunk_dict[intf] = vlan
    return (access_dict, trunk_dict)

print(get_int_vlan_map('config_sw2.txt'))