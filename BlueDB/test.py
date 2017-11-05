#tests

from __init__ import *

class Test:

    def __init__(self):
        self.test_1()
        self.test_2()
        self.test_3()
        self.test_4()

    def test_1(self):
        #testing __setitem__ and __getitem__ from Blue
        blue = Blue('test')
        blue['test_1'] = 'test_1'
        print(blue)
        print(blue['test_1'])
        print('\n')


    def test_2(self):
        #testing __setitem__ and __getitem__ with nested dicts
        blue = Blue('test')
        blue['test_2'] = {}
        blue['test_2']['nested_test'] = 'test_2'
        print(blue)
        print(blue['test_2'])
        print(blue['test_2']['nested_test'])
        print('\n')

    def test_3(self):
        #reserved
        pass

    def test_4(self):
        #reserved
        pass

if __name__ == '__main__':
    Test()
