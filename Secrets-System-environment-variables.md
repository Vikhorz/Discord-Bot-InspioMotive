# Secrets ( System Environment Variables ) Replit/Pyhton 


- A common way to give your application access to this information without leaking it to others is to store it in environment variables. With Replit, you can add environment variables as key-value pairs, and then read these values from your backend code.

- Environment Variables in Python – Read, Print, Set Environment variables is the set of key-value pairs for the current user environment. They are generally set by the operating system and the current user-specific configurations.

## To use Secrets in Python:

- Add the imports 
```python
import os
```
- Access the secret by key as an environment variable 
```python
my_secret = os.environ('key name')
```
or 
```python
my_secret = os.getenv('key name')
```
