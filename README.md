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
