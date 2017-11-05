# BlueDB
*a better shelves!*

##  What is BlueDB
BlueDB is a dictionary type in-memory database (like shelve but better and faster.) It uses pickle to dump and load keys to dicts to `.blue` files.  It runs faster and better than shelves

### Why use BlueDB
BlueDB is a fast-er and easy to use database

### Why not use BlueDB
BlueDB is still being tested and worked on so dont be supprised if you see any bugs anywhere...

## Examples
```python
from BlueDB import *

db = Blue('database')

db['key'] = 'value'
print(db['key'])

db['key'] = {}
db['key']['another key'] = 'another value'
print(db)
db['key']['another key'] = 'yet another value'
print(db)

>>> value
>>> {'key': {'another key': 'another value'}}
>>> {'key': {'another key': 'yet another value'}}
```

## To-Do

- [ ] Work on other data types.
- [ ] Clean up code.
- [ ] Make faster.
- [x] Have no dependencies :)
