#blue
"""
STATUS: FINISHED
CURRENT BUILD: dumping
FINAL BUILD: Blue3
"""

import ujson
import sys
import os

class Blue:

    def __init__(self, name):
        self.name = name
        self.file = name+'.bluI1'

        self.cache = {}

        try:
            with open(self.file, 'r') as fp:
                ujson.load(fp)
        except:
            with open(self.file, 'w') as fp:
                ujson.dump({}, fp)

        self.check()

    def mem(self):
        return sys.getsizeof(self.cache)

    def check(self):
        if len(self.cache) == 0:
            self.pushed = True
        else:
            self.pushed = False

    def __getitem__(self, key):
        try:
            return self.cache[key]
        except:
            return self.get_from_disk(key)

    def get_from_disk(self, key):
        with open(self.file, 'r') as fp:
            data = ujson.load(fp)
        return data[key]

    def get_all(self):
        if self.pushed is False:
            self.push_all()
        else:
            pass
        with open(self.file, 'r') as fp:
            data = ujson.load(fp)
        return data

    def __setitem__(self, key, value):
        self.push_mem(key, value)

    def push_mem(self, key, value):
        if self.mem() > 1e5:
            while self.mem() > 1e5:
                popped = self.cache.popitem()
                self.push_disk(popped[0], popped[1])
        else:
            self.cache[key] = value
        self.check()

    def push_disk(self, key, value):
        with open(self.file, 'r') as fp:
            data = ujson.load(fp)

        data[key] = value
        if key in self.cache.keys():
            del self.cache[key]

        with open(self.file, 'w') as fp:
            ujson.dump(data, fp)

    def push_all(self):
        for i in list(self.cache.keys()):
            self.push_disk(i, self.cache[i])

    def __delitem__(self, key):
        if key in self.cache.keys():
            del self.cache[key]
        elif key in self.get_all().keys():
            with open(self.file, 'r') as fp:
                data = ujson.load(fp)
            del data[key]
            with open(self.file, 'w') as fp:
                ujson.dump(data, fp)
        else:
            raise KeyError(f'{key}')

    def __del__(self):
        self.push_all()

    def __repr__(self):
        if len(self.get_all()) == 0:
            return str(dict())
        else:
            return str(self.get_all())
