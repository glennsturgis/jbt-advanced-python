# Python Advanced Course by JB

Extra Resources:  
https://book.pythontips.com/en/latest/#  
http://www.dabeaz.com/coroutines/Coroutines.pdf  
https://stackoverflow.com/questions/19302530/whats-the-purpose-of-send-function-on-python-generators  
yield from explanation - https://stackoverflow.com/questions/9708902/in-practice-what-are-the-main-uses-for-the-yield-from-syntax-in-python-3-3  

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

## Day 4
- **pytest**
  - https://semaphoreci.com/community/tutorials/testing-python-applications-with-pytest
- virtual environments - `venv`
  - `sys.executable` - the python that will run by default in the current context
  - https://stackoverflow.com/questions/41573587/what-is-the-difference-between-venv-pyvenv-pyenv-virtualenv-virtualenvwrappe
  - pip install only manual dependencies - https://pypi.org/project/pip-chill/
- Folder structure
  - Project
    - project/app
    - test
    - ...
- Coding Principles
  - TDD - Test Driven Development
    - use tests to defined how code logic behaves
  - Clean Code - http://cleancoder.com/products
  - SOLID
    - https://medium.com/backticks-tildes/the-s-o-l-i-d-principles-in-pictures-b34ce2f1e898
  - Design Patterns
    - Serve the purpose of adhering to SOLID patterns where each pattern implements a specific purpose.
    - https://python-patterns.guide/
    - https://www.digitalocean.com/community/tutorials/gangs-of-four-gof-design-patterns
