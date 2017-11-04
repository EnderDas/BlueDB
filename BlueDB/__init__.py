#__init__

__name__ = 'BlueDB'
__version__ = '0.0.1'

import pickle

class Blue(dict):

    def __init__(self, name, **kwargs):
        super().__init__()
        self.name = name

        self.__load__()

        self.__attri__ = [] #for a attribute type system, no use for now

    def __load__(self):
        try:
            data = pickle.load(open(f'{self.name}.blue', 'rb'))
            self = data
        except:
            pickle.dump(self, open(f'{self.name}.blue', 'wb'))
            return

    def __setitem__(self, name, value):

        self.__dict__[name] = value
        self[name] = value

        with open(f'{self.name}.blue', 'wb') as thing:
            pickle.dump(self, thing)

    def __getitem__(self, name): #Too many try/excepts for me too look at...
        try:
            return self[name]
        except:
            try:
                return self.__dict__[name]
            except:
                try:
                    with open(f'{self.name}.blue', 'rb') as thing:
                        thingy = pickle.load(thing)
                    return thingy.__dict__[name]
                except:
                    raise KeyError(f"Key '{name}' does not exist.")
