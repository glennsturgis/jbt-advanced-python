from collections import defaultdict
import statistics
from typing import List

DATA_FILE = r'C:\Users\jbt\Desktop\jbt-advanced-python\day-1\exercise-0\data\diamonds.csv'


class Diamond:
    """Represents a diamond class"""

    # TODO: initialize arguments dynamically
    """
    ===
    Option 1
    ===
    class DiamondMeta(type):
    def __new__(cls, name, bases, dct):
        for name, value in defaults.items():
            dct[name] = some_complex_init_function(value, ...)
        return type.__new__(cls, name, bases, dct)

    class Diamond(object):
        __metaclass__ = DiamondMeta
    
    ===
    Option 2
    ===
    use settatr when iterating over the kwargs
    
    ===
    Option 3
    ===
    set __dict__ to be kwargs
    """

    def __init__(self, id, carat, cut, color, clarity, depth, table, price, x, y, z):
        self.id = id
        self.carat = float(carat)
        self.cut = cut
        self.color = color
        self.clarity = clarity
        self.depth = float(depth)
        self.table = float(table)
        self.price = float(price)
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)


class DiamondsIter:

    def __init__(self, diamonds):
        self.diamonds = diamonds
        self._index = 0
        self._size = len(diamonds.diamonds)

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < self._size:
            current_index = self._index
            self._index += 1
            return self.diamonds.diamonds[current_index]
        raise StopIteration


class Diamonds:
    """Represents a collection of diamonds"""

    def __init__(self, diamonds: List[Diamond]) -> None:
        self.diamonds = diamonds

    def __iter__(self):
        return DiamondsIter(self)

    def __str__(self):
        return self.__dict__


def average_key_by_group(group, key, diamonds):
    groups = defaultdict(list)
    for diamond in diamonds:
        groups[getattr(diamond, group)].append(getattr(diamond, key))

    return {group: statistics.mean(keys) for group, keys in groups.items()}


def main():
    with open(DATA_FILE) as f:
        diamonds_raw = f.readlines()

    diamonds = Diamonds([Diamond(*line.split(',')) for line in diamonds_raw[1:]])

    print(f'1. The most expensive diamond is: {max([diamond.price for diamond in diamonds])}')
    print(f'2. The average price of a diamond is: {statistics.mean([diamond.price for diamond in diamonds])}')
    print(
        f'3. The number of diamonds with cut "Ideal" is : {len([diamonds for diamond in diamonds if "Ideal" in diamond.cut])}')
    colors = set([diamond.color for diamond in diamonds])
    print(f'4. There are {len(colors)} colors, which are: {",".join(sorted(colors))}')
    print(
        f'5. The median carat for "Premium" diamonds is: {statistics.median([diamond.carat for diamond in diamonds if "Premium".lower() in diamond.cut.lower()])}')
    print(f"6. The average carats per cut {average_key_by_group('cut', 'carat', diamonds)}")
    print(f"7. The average price per color {average_key_by_group('color', 'price', diamonds)}")

    with open(r'C:\Users\jbt\Desktop\jbt-advanced-python\day-1\exercise-0\data\price_and_carat.csv', 'a') as f:
        f.write('price,carat\n')
        f.writelines([f'{diamond.price},{diamond.carat}\n' for diamond in diamonds])


if __name__ == '__main__':
    main()
