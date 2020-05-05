#!/usr/bin/python -tt
# Project: pyATS_Community_Solutions
# Filename: nornir_get_genie_parse
# claudia
# PyCharm

from __future__ import absolute_import, division, print_function

__author__ = "Claudia de Luna (claudia@indigowire.net)"
__version__ = ": 1.0 $"
__date__ = "5/5/20"
__copyright__ = "Copyright (c) 2018 Indigo Wire Networks"
__license__ = "Python"

import argparse
from nornir import InitNornir
from nornir.plugins.tasks.networking import netmiko_send_command
from nornir.plugins.functions.text import print_result


def main():

    # Create instance using default hosts.yaml and groups.yaml
    nr = InitNornir(config_file='config.yaml')

    # print(dir(nr))
    print("Hosts derived from the Inventory file are: \t{}".format(nr.inventory.hosts))
    print("Groups derived from the Inventory file are: \t{}".format(nr.inventory.groups))

    print("\nDecomposing Groups...")
    my_groups = nr.inventory.groups
    group_keys = list(my_groups.keys())
    print("Group keys = {} of type {} ".format(group_keys, type(group_keys)))
    for i in group_keys:
        print(f"- {i}")

    print("\nDecomposing Hosts...")
    my_hosts = nr.inventory.hosts
    print("Type of nr.inventory.hosts in var my_hosts is {}".format(type(my_hosts)))

    host_keys = list(my_hosts.keys())
    print("Host keys = {} of type {} ".format(host_keys, type(host_keys)))
    for i in host_keys:
        print(f"- {i}")

    print("\n")

    show_command = arguments.command
    print(f"Logging into hosts in inventory and executing show command...")

    result = nr.run(netmiko_send_command, command_string=show_command)

    print(f"command output stored in the varialbe 'result'...")

    # Printing now may help you decompose the resulting objects
    # print(result)
    # print(dir(result))

    print(f"\nDecomposing Nornir Result Object of type {type(result)}...\n")
    print(result.items())
    print(result.values())
    print(result.keys())

    for k in result.keys():
        print(f"\n=================== DEVICE {k} ===================")
        print(k)
        print(result[k])
        print(dir(result[k]))
        output = result[k][0]
        print(f"\nOutput of MultiResult First Element: \n{output}")
        print(f"\n=================== END DEVICE {k} ===================")


# Standard call to the main() function.
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Script Description",
                                     epilog="Usage: ' python nornir_get_genie_parse.py' ")

    parser.add_argument('-c', '--command', help='Execute this show command. Default: show ip int brief', action='store',
                        default='show version')
    arguments = parser.parse_args()
    main()
