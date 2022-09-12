# simple iterator

class SimpleIterator:

    def __init__(self, limit=0):
        self._counter = 0
        self._limit = limit

    def __next__(self):
        """
        In a loop, this is called next(self)
        """
        self._counter += 1
        if self._counter < 10:
            return self._counter
        raise StopIteration

    def _reset(self):
        self._counter = 0

    def __iter__(self):
        """
        Gets called when iterating on an object
        """
        # in order to allow for multiple iteration, you can add a reset.
        # self._reset()
        return self


if __name__ == '__main__':
    mr = SimpleIterator()

    print(*mr, sep=', ', end='\n')
    print('second time')
    print(*mr, sep=', ', end='\n')  # doesn't print anything as iterator was exhausted
