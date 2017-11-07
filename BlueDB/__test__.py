from __init__ import Blue
import shelve, chest, os
from timeit import default_timer as timer

test_dict_one = {
    "test_key": {
        "nested_test_key": "nested_test_value"
    }
}

test_dict_two = {
    "test_key": "test_value"
}


def __test_blue__():
    start = timer()
    blue = Blue('test')
    blue['test_dict'] = test_dict_one
    print(blue['test_dict'])
    blue['test_dict']['test_key'] = test_dict_two
    print(blue['test_dict'])
    end = timer()
    os.remove('test.blue')
    print('blue', end-start)

def __test_shelve__():
    start = timer()
    shelf = shelve.open('test', writeback=True)
    shelf['test_dict'] = test_dict_one
    print(shelf['test_dict'])
    shelf['test_dict']['test_key'] = test_dict_two
    print(shelf['test_dict'])
    shelf.close()
    end = timer()
    os.remove('test.dat')
    os.remove('test.dir')
    print('shelve', end-start)

def __test_chest__():
    start = timer()
    box = chest.Chest(path='test')
    box['test_dict'] = test_dict_one
    print(box['test_dict'])
    box['test_dict']['test_key'] = test_dict_two
    print(box['test_dict'])
    end = timer()
    print('chest', end-start)

__test_chest__()
__test_blue__()
__test_shelve__()
