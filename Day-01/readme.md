# Day-01 Python Getting Started
## What script1.py all about ?
script1.py is all about
1. How to print anything
2. How to represent string in python
3. How to take input
4. How to debug using print

## [Comments | Python for Beginners [7 of 44]](https://www.youtube.com/watch?v=kEuVvUc1Zec&list=PLlrxD0HtieHhS8VzuMCfQD4uJ9yne1mE6&index=7&ab_channel=MicrosoftDeveloper)

We add comments to our code using #
```python
# This is a comment in my code it does nothing
```

Commenting helps to find the isuue in your code.

```python
print('hello it's a small world')
```

If you run this code, you will get 
```
Traceback (most recent call last):
  File "/Users/sanketkumarpanda/.vscode/extensions/ms-python.python-2024.10.0-darwin-x64/python_files/python_server.py", line 117, in exec_user_input
    retval = callable(user_input, user_globals)
  File "<string>", line 1
    print('hello it's a small world')
                    ^
SyntaxError: invalid syntax
```
So to fix the issue, you can copy the code and paste it below, put the comment on the above line and now change the singule quote to double you will see the code is working well. So commenting helps in keep the previous version of code, while updating it in the next version.

```python
# This is a comment in my code it does nothing
# print('hello it's a small world')
print("hello it's a small world")
```
