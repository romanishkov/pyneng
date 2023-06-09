# -*- coding: utf-8 -*-

"""
Задание 24.2b

Скопировать класс MyNetmiko из задания 24.2a.

Дополнить функционал метода send_config_set netmiko и добавить в него проверку
на ошибки с помощью метода _check_error_in_command.

Метод send_config_set должен отправлять команды по одной и проверять каждую на ошибки.
Если при выполнении команд не обнаружены ошибки, метод send_config_set возвращает
вывод команд.

In [2]: from task_24_2b import MyNetmiko

In [3]: r1 = MyNetmiko(**device_params)

In [4]: r1.send_config_set('lo')
---------------------------------------------------------------------------
ErrorInCommand                            Traceback (most recent call last)
<ipython-input-2-8e491f78b235> in <module>()
----> 1 r1.send_config_set('lo')

...
ErrorInCommand: При выполнении команды "lo" на устройстве 192.168.100.1 возникла ошибка "Incomplete command."

"""
from netmiko.cisco.cisco_ios import CiscoIosSSH
import re

class ErrorInCommand(Exception):
    """
    Исключение генерируется, если при выполнении команды на оборудовании,
    возникла ошибка.
    """

class MyNetmiko(CiscoIosSSH):
    def __init__(self, **device_params):
        super().__init__(**device_params)
        self.enable()

    def send_command(self, command):
        result = super().send_command(command)
        self._check_error_in_command(command, result)
        return result

    def send_config_set(self, commands):
        result_all = ''
        if type(commands) == str:
            commands = [commands]
        commands = [*commands, 'end']
        for command in commands:
            result = super().send_config_set(command, exit_config_mode=False)
            self._check_error_in_command(command, result)
            result_all += result
        return result_all

    def _check_error_in_command(self, command, result):
        regex = "% (?P<errmsg>.+)"
        template = 'При выполнении команды "{}" на устройстве {} возникла ошибка -> {}'
        failed = re.search(regex, result)
        if failed:
            raise ErrorInCommand(template.format(command, self.host, failed.group("errmsg")))


if __name__ == "__main__":
    device_params = {
        "device_type": "cisco_ios",
        "ip": "192.168.100.1",
        "username": "cisco",
        "password": "cisco",
        "secret": "cisco",
    }
    ssh = MyNetmiko(**device_params)
    print(ssh.send_config_set("int lo1"))