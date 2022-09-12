# Python Advanced Course by JB

## Day 1
- Python Refresher

## Day 2
- Functions and Advanced Functions
- Scope
  - global - module level
  - nonlocal - function level (closures, decorators, etc..)
  - local* - same scope
- Closures
- Decorators
- Lambdas - `lambda x: x + 1`
- Docstrings and Annotations - `__doc__`, `__annotations__`
- OOP

## Day 3
- map, filter, reduce - use a function on an iterable
- comprehensions - pythonic way to replace map and filter
- iterators
  - allow for objects to be iterable - `iter(...)` returns and iterator (calls `__iter__`)
  - `iter` function makes iterables iterators
  - must implement:
    - `__next__` which produces the next item in the iteration and raise `StopIteration` exception at the end of the iteration
    - `__iter__` which is an iterator object
- generators
- Modules
  - adding modules to `sys.path` will be global
- Packages
  - .pypirc (pypi config)
  - .setup.cfg and setup.py
- exceptions
- multithreading
  - runs in a single process
  - create thread, start thread and 'wait' for thread `join`
- multiprocessing
  - runs in multiple processes