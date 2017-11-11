# BlueDB
*use my database, is good!*

```python
>>> from BlueDB import Blue
>>> database = Blue('database')
>>> database['key'] = {'nested key': 'nested value'}
>>> print(database['key']['nested key'])
nested value
>>> database['key']['nested key'] = 'new value'
>>> print(database)
{'key': {'nested key': 'new value'}}
```

##

`py -m pip install BlueDB` to install it then import `Blue` class and you're good to go!


### Blue2

[Blue2](BlueDB/blue2.py) is a subset of BlueDB using [ujson](https://github.com/esnme/ultrajson) to make handling large databases faster and better
>most likely will become the default BlueDB in v0.4 or v0.3

Currently Blue2 is smaller and much cleaner than BlueDB, but not as complete as I want it to be.  im also working on a more controllable and customizable Database system that will be in Blue2 but not released until v0.3. BlueDB will be kept how it is until I complete Blue2.

#### To Use
> ujson is needed to use Blue2!  To get ujson just do `py -m pip install ujson`
```py
>>> from BlueDB.blue2 import Blue
>>> database = Blue('test') #very JSON wow!
>>> database['key'] = 'some value'
>>> print(database)
{'key': 'some value'}
```

### Benchmarks

The current speed benchmarks are based upon setting a dict from a 4Mb .json file and then getting that dict back. The libs that are compared are, BlueDB, BlueDB(Blue2), Chest, and buitlin Shelve.  BlueDB isnt great for parsing large librarys hense the reason im working on Blue2.

```py
('blue', 0.9652696128473567)
('blue2', 0.31672797164887256)
('chest', 0.005320636684295499)
('shelve', 0.678065958485849)
```
