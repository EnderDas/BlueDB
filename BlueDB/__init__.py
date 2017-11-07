#Better BlueDB
try:
    import ujson as json
except:
    import json

class Blue:

    def __init__(self, name, path = None, **kwargs):
        self.name = name
        self.file = self.name+'.blue'

        self._load = kwargs.pop('load', json.load)
        self._dump = kwargs.pop('dump', json.dump)

        try:
            with open(self.file, 'r') as fp:
                data = self._load(fp)
            self.super_ = data
            self.items_ = self.super_['items']
        except:
            with open(self.file, 'w') as fp:
                self._dump({}, fp)
            self.super_ = {'name': self.name, 'items': {}}
            self.items_ = {}

    def __getitem__(self, key):
        try:
            return self.items_[key]
        except:
            with open(self.file, 'r') as fp:
                data = self._load(fp)['items']
                return data[key]

    def __setitem__(self, key, value):
        self.items_[key] = value
        self.super_['items'][key] = value
        with open(self.file, 'w') as fp:
            self._dump(self.super_, fp)

    def __delitem__(self, key):
        del self.items_[key]
        del self.super_['items'][key]
        with open(self.file, 'w') as fp:
            self._dump(self.super_, fp)

    def __repr__(self):
        return str(self.items_)

    def __str__(self):
        return str(self.items_)

if __name__ == '__main__':
    from timeit import default_timer as timer
    import shelve
    import os
    start = timer()
    s = shelve.open('test', writeback = True)
    s['l'] = {'a': 1}
    print(s['l'])
    s['l']['a'] = 2
    print(s['l'])
    s.close()
    end = timer()
    print('shelve', end-start)
    start = timer()
    b = Blue('test')
    b['l'] = {'a': 1}
    print(b)
    b['l']['a'] = 2
    print(b)
    end = timer()
    print('blue', end-start)
    os.remove('test.bak')
    os.remove('test.blue')
    os.remove('test.dat')
    os.remove('test.dir')
