from enum import Enum
import pathlib


class Severity(Enum):
    DEBUG = 1
    INFO = 2
    ERROR = 3


class LogReader:

    def __init__(self, num_of_lines: int, severity: int):
        self._num_of_lines = num_of_lines
        self._severity = severity
        self._file_path = r'C:\Users\jbt\PycharmProjects\jbt-advanced-python\day-2\exercise-1\data\example-log.txt'
        self._file = self._open_file(self._file_path)

    @property
    def num_of_lines(self):
        return self._num_of_lines

    @num_of_lines.setter
    def num_of_lines(self, num_of_lines):
        self._num_of_lines = num_of_lines

    @property
    def severity(self):
        return self._severity

    @severity.setter
    def severity(self, severity):
        self._severity = severity

    @staticmethod
    def _open_file(path):
        if pathlib.Path(path).exists():
            return open(path)
        raise FileNotFoundError()

    def __enter__(self):
        self._open_file(self._file_path)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._file.close()

    def close(self):
        self.__exit__(None, None, None)

    def gen(self):
        count = 0
        lines = []
        for line in self._file:
            if Severity(self._severity).name in line:
                count += 1
                lines.append(line)
            if count == self._num_of_lines:
                yield lines
                lines.clear()
                count = 0
        yield lines


if __name__ == '__main__':
    with LogReader(5, 1) as log_reader:
        lines = log_reader.gen()
        print(next(lines, 'Done iterating'))
        print(next(lines, 'Done iterating'))
        print(next(lines,'Done iterating'))
        # print(*lines, end='\n', sep='')
