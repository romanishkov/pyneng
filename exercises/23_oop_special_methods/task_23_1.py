# -*- coding: utf-8 -*-

"""
Задание 23.1

В этом задании необходимо создать класс IPAddress.

При создании экземпляра класса, как аргумент передается IP-адрес и маска,
а также должна выполняться проверка корректности адреса и маски:
* Адрес считается корректно заданным, если он:
   - состоит из 4 чисел разделенных точкой
   - каждое число в диапазоне от 0 до 255
* маска считается корректной, если это число в диапазоне от 8 до 32 включительно

Если маска или адрес не прошли проверку, необходимо сгенерировать
исключение ValueError с соответствующим текстом (вывод ниже).

Также, при создании класса, должны быть созданы два атрибута экземпляра:
ip и mask, в которых содержатся адрес и маска, соответственно.

Пример создания экземпляра класса:
In [1]: ip = IPAddress('10.1.1.1/24')

Атрибуты ip и mask
In [2]: ip1 = IPAddress('10.1.1.1/24')

In [3]: ip1.ip
Out[3]: '10.1.1.1'

In [4]: ip1.mask
Out[4]: 24

Проверка корректности адреса (traceback сокращен)
In [5]: ip1 = IPAddress('10.1.1/24')
---------------------------------------------------------------------------
...
ValueError: Incorrect IPv4 address

Проверка корректности маски (traceback сокращен)
In [6]: ip1 = IPAddress('10.1.1.1/240')
---------------------------------------------------------------------------
...
ValueError: Incorrect mask

"""
import re


class IPAddress:
    def __init__(self, ip_in):
        ip_slash_mask_regexp = r'^(?P<ip_str>\S+)/(?P<mask_str>\d+)$'
        ip_mask_search = re.search(ip_slash_mask_regexp, ip_in)
        if ip_mask_search:
            mask = ip_mask_search.group('mask_str')
            ip = ip_mask_search.group('ip_str')
            self._check_ip(ip)
            self._check_mask(mask)
            self.ip, self.mask = ip, int(mask)
        else:
            raise ValueError("Wrong format")

    def _check_ip(self, ip):
        octets = ip.split(".")
        correct_octets = [
            octet for octet in octets if octet.isdigit() and 0 <= int(octet) <= 255
        ]
        if len(octets) == len(correct_octets) == 4:
            return True
        else:
            raise ValueError("Incorrect IPv4 address")

    def _check_mask(self, mask):
        if mask.isdigit() and 8 <= int(mask) <= 32:
            return True
        else:
            raise ValueError("Incorrect mask")


if __name__ == "__main__":
    ip = IPAddress('10.1.1/26')
    print(ip.ip)
    print(ip.mask)
