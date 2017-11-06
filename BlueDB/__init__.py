#__init__

__version__ = '0.1.3'

from _pickle import Pickler, Unpickler

class Blue:

    def __init__(self, name, **kwargs):

        self.name = name
        self.__vars__ = {}
        self.__blues__ = {}

        try:
            with open(f'{self.name}.blue', 'rb') as fp:
                p = Unpickler(fp)
                q = p.load()
                self.__vars__ = q.__vars__
                self.__blues__ = q.__blues__
                self.__loaded__ = q
        except:
            with open(f'{self.name}.blue', 'wb') as fp:
                p = Pickler(fp)
                p.dump(self)

    def __repr__(self):
        return str(self.__vars__)

    def __setitem__(self, key, value):
        if type(value) is dict:
            blue = Blue_dict(key, value, self, self)
            self.__vars__[key] = blue
            self.__blues__[key] = blue
            with open(f'{self.name}.blue', 'wb') as fp:
                p = Pickler(fp)
                p.dump(self)
        else:
            self.__vars__[key] = value
            with open(f'{self.name}.blue', 'wb') as fp:
                p = Pickler(fp)
                p.dump(self)
        self.__base_reload__()

    def __getitem__(self, key):
        try:
            return self.__vars__[key]
        except:
            try:
                with open(f'{self.name}.blue', 'rb') as fp:
                    p = Unpickler(fp)
                    data = p.load().__vars__.get(key)
                if data is None:
                    raise
                else:
                    return data
            except:
                raise KeyError(f"Key '{key}' does not exist.")

    def __delitem__(self, key):
        del self.__vars__[key]
        with open(f'{self.name}.blue', 'wb') as thing:
            p = Pickler(thing)
            p.dump(self)
        self.__base_reload__()

    def __base_reload__(self):
        #VERY MESSY
        better_blue = Blue(self.name)
        for l in better_blue.__vars__.keys():
            for i in self.__vars__.keys():
                if l == i:
                    if self.__vars__[i] == better_blue.__vars__[i]:
                        pass
                    else:
                        self.__vars__[i] = better_blue.__vars__[i]
                else:
                    pass

class Blue_dict:

    def __init__(self, key, value, previous, core, **kwargs):
        self.__key__ = key
        self.__previous__ = previous
        self.__core__ = core
        self.__blues__ = {}
        if len(value) > 0:
            self.__vars__ = {}
            for i in value.keys():
                if type(value[i]) == dict:
                    self.__setitem__(i, value[i])
                else:
                    self.__vars__[i] = value[i]
        else:
            self.__vars__ = dict(value)


    def __setitem__(self, name, value):
        if type(value) is dict:
            blue = Blue_dict(name, value, self, self.__core__)
            self.__vars__[name] = blue
            self.__blues__[name] = blue
            self.__previous__.__setitem__(self.__key__, self.__vars__)
        else:
            self.__vars__[name] = value
            self.__previous__.__setitem__(self.__key__, self.__vars__)

    def __delitem__(self, name):
        del self.__vars__[name]

    def __iter__(self):
        return iter(self.__vars__)

    def __len__(self):
        return len(self.__vars__)

    def __repr__(self):
        return str(self.__vars__)

    def __getitem__(self, name):
        return self.__vars__[name]

class Blue_list:

    def __init__(self, key, value, previous, core, **kwargs):
        raise NotImplementedError
        self.__key__ = key #indice
        self.__vars__ = list(value)
        self.__blues__ = {}
        self.__core__ = core

    def __repr__(self):
        return str(self.__vars__)
