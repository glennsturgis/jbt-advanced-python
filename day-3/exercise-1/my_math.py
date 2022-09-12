_is_initialized = False

def initlib():
    global _is_initialized
    _is_initialized = True


def min(a, b):
    return a if a <= b else b

def max(a, b):
    return a if a >= b else b

def mean(numbers):
    return sum(numbers) / len(numbers)


initlib()