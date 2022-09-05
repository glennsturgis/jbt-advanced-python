import statistics


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