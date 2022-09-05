from itertools import count
from collections import defaultdict
import statistics


DATA_FILE = r'C:\Users\jbt\Desktop\jbt-advanced-python\day-1\exercise-0\data\diamonds.csv'


class Diamond:
    """Represents a diamond class"""
    "","carat","cut","color","clarity","depth","table","price","x","y","z"
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
      
def find_most_expensive_diamond(diamonds):
    return max([diamond.price for diamond in diamonds])

def find_average_diamond_price(diamonds):
    return statistics.mean([diamond.price for diamond in diamonds])

def count_by_cut(key, diamonds):
    return len([diamonds for diamond in diamonds if key.lower() in diamond.cut.lower()])

def get_colors(diamonds):
    return set([diamond.color for diamond in diamonds])

def get_median_carat_by_key(key, diamonds):
    return statistics.median([diamond.carat for diamond in diamonds if key.lower() in diamond.cut.lower()])

def average_key_by_group(group, key, diamonds):
    groups = defaultdict(list)
    for diamond in diamonds:
        groups[getattr(diamond, group)].append(getattr(diamond, key))

    return {group: statistics.mean(keys) for group, keys in groups.items()}

def main():
    with open(DATA_FILE) as f:
        diamonds_raw = f.readlines()

    
    diamonds = [Diamond(*line.split(',')) for line in diamonds_raw[1:]]

    print(f'1. The most expensive diamond is: {find_most_expensive_diamond(diamonds)}')
    print(f'2. The average price of a diamond is: {find_average_diamond_price(diamonds)}')
    print(f'3. The number of diamonds with cut "Ideal" is : {count_by_cut("Ideal", diamonds)}')
    colors = get_colors(diamonds)
    print(f'4. There are {len(colors)} colors, which are: {",".join(colors)}')
    print(f'5. The median carat for "Premium" diamonds is: {get_median_carat_by_key("Premium", diamonds)}')
    print(f"6. The average carats per cut {average_key_by_group('cut', 'carat', diamonds)}")
    print(f"7. The average price per color {average_key_by_group('color', 'price', diamonds)}")

if __name__ == '__main__':
    main()