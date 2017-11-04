#__init__

class Blue(dict):

    def __init__(self, name, **kwargs):
        super().__init__()
        self.name = name

        self.__load__()

    def __load__(self):
        try:
            data = pickle.load(open(self.name, 'rb'))
            self = data
        except:
            pickle.dump(self, open(self.name, 'wb'))
            return

    def __setitem__(self)
