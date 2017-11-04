#__init__

__version__ = '0.0.1'

from pickle import Pickler, Unpickler

class Blue_dict(dict):

    def __init__(self, value, **kwargs):
        super().__init__(**kwargs)
# ^ this is something that will fix __setitem__ when it comes to nested dicts
# not finished with it yet

class Blue:

    def __init__(self, name, **kwargs):

        self.name = name
        self.__vars__ = {}
        try:
            with open(self.name, 'rb') as fp:
                p = Unpickler(fp)
                self.__vars__ = p.load().__vars__
        except:
            with open(self.name, 'wb') as fp:
                p = Pickler(fp)
                p.dump(self)
                
    def __repr__(self):
        return str(self.__vars__)

    def __setitem__(self, key, value):
        self.__vars__[key] = value
        with open(self.name, 'wb') as fp:
            p = Pickler(fp)
            p.dump(self)

    def __getitem__(self, key):
        with open(self.name, 'rb') as fp:
            p = Unpickler(fp)
            data = p.load().__vars__[key]
        return data
