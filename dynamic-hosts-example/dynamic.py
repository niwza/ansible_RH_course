#!/usr/bin/env python

import os
import  argparse
import sys

try:
    import json
except ImportError:
    import simplejson as json

class OurInventory(object):

    def __init__(self):
        self.inventory = {}
        self.read_cli_args()

        if self.args.list:
            self.inventory = self.our_inventory()
        elif self.args.host:
            self.inventory = self.empty_inventory()
        else:
            self.inventory = self.empty_inventory()

        print json.dumps(self.inventory)

    def our_inventory(self):
        return {
            'group': {
                'hosts': ['server', 'host1', 'host2'],
                'vars': {
                    'ansible_user': 'ansible',
                    'test_variable': 'nonspecific_value'
                }
            },
            '_meta': {
                'hostvars': {
                    'host1': {
                        'logs_folder': '/var/log'
                    },
                    'host2': {
                        'logs_folder': '/var/log2'
                    }
                }
            }
        }

    def empty_inventory(self):
        return {'_meta': {'hostvars': {}}}

    def read_cli_args(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('--list', action = 'store_true')
        parser.add_argument('--host', action = 'store')
        self.args = parser.parse_args()

OurInventory()