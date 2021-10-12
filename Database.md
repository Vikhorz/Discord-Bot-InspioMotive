# Replit Database

- For the Database I used the online Replit Database.
- (https://replit.com), (https://docs.replit.com/misc/database).

## COMMANDS:

- Import the database:  
```python
from replit import db
```
- Set a key to a value:  
```python
db["key"] = "value"
```
- Get a key's value:  
```python
value = db["key"]
```
- Delete a key:  
```python
del db["key"]
```
- List all keys:  
```python 
keys = db.keys()
```
- List keys with a prefix:  
```python 
matches = db.prefix("prefix")
```
