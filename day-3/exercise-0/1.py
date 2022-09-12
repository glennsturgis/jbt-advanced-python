import random

l = list(range(1, 21))


def gen_random_int(min, max):
    """
    Generates a random number between min and max
    """
    while True:
        values = yield random.randint(min, max)
        print('Sent Values', values)
        if values is not None:  # check if None for when to initialize generator
            min, max = values

def gen_circular(num):
    """
    Generates a number in a circular fashion between 0 and num
    0,1,2,3..num, num-1...num-n, 0, 1, 2, 3...
    """
    current = 0
    asc = True
    while True:
        if current == 0:
            asc = True
        elif current == num:
            asc = False

        if asc:
            current += 1
        else:
            current -= 1
        yield current


def gen_log_level(num_of_line, severity):
    log_file = r'C:\Users\jbt\Desktop\jbt-advanced-python\day-3\data\example-log.txt'
    with open(log_file) as f:
        for line_num, line in enumerate(f):
            prefix = int(line[0].strip()) if line[0].strip() else 0
            if prefix <= severity:
                values = yield line
            if values is not None:
                num_of_line, severity = values

            if line_num == num_of_line:
                break



if __name__ == '__main__':
    print(f'odd: {[i % 2 == 1 for i in l]}')
    print(f'mul10: {[i * 10 for i in l]}')

    random_ints = gen_random_int(5, 10)
    print(f'random numbers: {next(random_ints)}')
    print(f'random numbers: {next(random_ints)}')
    print(f'random numbers: {next(random_ints)}')
    print('=' * 80)
    random_ints.send(None)
    print(f'random numbers: {random_ints.send((1, 100))}')
    print(f'random numbers: {random_ints.send((101, 999))}')
    print(f'random numbers: {random_ints.send((-500, -200))}')

    circ = gen_circular(3)
    print(f'random numbers: {next(circ)}')
    print(f'random numbers: {next(circ)}')
    print(f'random numbers: {next(circ)}')
    print(f'random numbers: {next(circ)}')
    print(f'random numbers: {next(circ)}')
    print(f'random numbers: {next(circ)}')
    print(f'random numbers: {next(circ)}')
    print(f'random numbers: {next(circ)}')
    print(f'random numbers: {next(circ)}')
    print(f'random numbers: {next(circ)}')
    print(f'random numbers: {next(circ)}')
    print(f'random numbers: {next(circ)}')

    ll = gen_log_level(2, 3)
    ll.send(None)
    for l in ll:
        print(l.strip())
        ll.send((4, 1))
