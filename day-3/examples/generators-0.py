# NOTES:
# examples of sending into generators
# https://stackoverflow.com/questions/19302530/whats-the-purpose-of-send-function-on-python-generators
# http://dabeaz.com/coroutines/
# yield from explanation - https://stackoverflow.com/questions/9708902/in-practice-what-are-the-main-uses-for-the-yield-from-syntax-in-python-3-3

# Create a prompt that sends line into generator and prints whether it contains numbers
def gen_echo():
    _EXIT = False

    while not _EXIT:
        line = yield
        if line is not None and not line.startswith('exit'):
            print(f'You said {line}')
        if line.lower().startswith('exit'):
            exit()

if __name__ == '__main__':
    prompt = gen_echo()
    prompt.send(None)
    while True:
        line = input('>>>')
        prompt.send(line)
