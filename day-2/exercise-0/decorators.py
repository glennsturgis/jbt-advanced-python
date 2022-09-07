import time


def myzip(iter_a, iter_b):
    """
    Receives two iterables and returns a list of tuples.
    Should function exactly like zip builtin
    """
    shortest_iter = iter_a if len(iter_a) <= len(iter_b) else iter_b
    return [(iter_a[index], iter_b[index]) for index in range(len(shortest_iter))]


def zip_wrapper(iter_a, iter_b):
    """
    Receives two iterables and returns a list of tuples.
    Should function exactly like zip builtin
    """

    return list(zip(iter_a, iter_b))


def genfilterby(n):
    """
    Receives a number and returns a filter function that receives a list that returns the filtered numbers
    """

    def inner(l):
        return [item for item in l if item % n == 0]  # filter(lambda item: item % n == 0, l)

    return inner


def gr_than(n):
    """
    Receives n and returns a function that tests whether a given number is greater than n
    """
    return lambda m: m > n


def validate_id(func):
    """
    Decorator to validate id number.
    A valid id number contains 9 digits only
    """
    _VALID_ID_LENGTH = 9

    def wrapper(id_number):
        id_str = f'{id_number}'
        return (id_str.isnumeric() and len(str(id_number)) == _VALID_ID_LENGTH and func(id_number)) or f'ID {id_number} is invalid'

    return wrapper


def validate_phonenumber(func):
    """
    Decorator to validate id number.
    A valid id number contains 9 digits only
    """

    def validate(phonenumber):
        _VALID_PN_LENGTH = 10
        _VALID_PREFIX = ['054', '052', '050']
        phonenumber_str = f'{phonenumber}'
        return phonenumber_str.isnumeric() and len(phonenumber_str) == _VALID_PN_LENGTH and phonenumber[:3] in _VALID_PREFIX

    def wrapper(phonenumber):
        return (validate(phonenumber) and func(phonenumber)) or f'NUMBER {phonenumber} is invalid'

    return wrapper


def timeit(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        res = func(*args, **kwargs)
        end_time = time.time()
        print(f'{func.__name__} took {end_time - start_time}s to run')
        return res

    return wrapper


@validate_id
def get_id(id_number):
    return f'ID: {id_number} is valid'


@validate_phonenumber
def get_phonenumber(phone_number):
    return f'NUMBER: {phone_number} is valid'


@timeit
def take_your_time(n):
    time.sleep(n)
    return 'Done'


if __name__ == '__main__':
    # Test myzip
    print(myzip(['a', 'b', 'c'], [1, 2, 3]))
    print(myzip('glenn', '123456678'))
    print(myzip('', '1432'))

    # Test zip_wrapper
    print(myzip(['a', 'b', 'c'], [1, 2, 3]))
    print(myzip('glenn', '123456678'))
    print(myzip('', '1432'))

    # test genfilterby
    filter_by_three = genfilterby(3)
    print(filter_by_three([1, 2, 3, 4, 5, 4, 5, 6, 7, 8, 9]))

    # test greater_than
    greater_than_five = gr_than(5)
    print(greater_than_five(3))
    print(greater_than_five(5))
    print(greater_than_five(10))

    # test validate_id
    print(get_id(123456789))
    print(get_id(123345))
    print(get_id(12345678912341324))

    # test validate_number
    print(get_phonenumber('0541234567'))
    print(get_phonenumber(int('0541234567')))
    print(get_phonenumber('0571234567'))
    print(get_phonenumber('+972123456'))
    print(get_phonenumber(123))

    # test timeit
    take_your_time(5)
    take_your_time(0)
    take_your_time(3)
