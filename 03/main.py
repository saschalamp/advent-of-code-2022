import functools

def get_same_item(first, second):
    for item in first:
        if item in second:
            return item
    return None

def get_priority(item):
    ord_value = ord(item)
    if ord("a") <= ord_value and ord_value <= ord("z"):
        ord_value = ord_value - ord("a") + 1
    if ord("A") <= ord_value and ord_value <= ord("Z"):
        ord_value = ord_value - ord("A") + 27
    return ord_value

def get_rucksack_priority(rucksack):
    l = len(rucksack)//2
    item = get_same_item(rucksack[:l], rucksack[l:])
    return get_priority(item)

def get_total_priority(input):
    return functools.reduce(lambda a, b: a + get_rucksack_priority(b), input, 0)

def get_badge(input):
    for item in input[0]:
        if item in input[1] and item in input[2]:
            return item
    return None

def get_total_badge_priority(input):
    return functools.reduce(lambda a, b: a + get_priority(get_badge(b)), TripleIterator(input), 0)

class TripleIterator:
    def __init__(self, items):
        self.items = items
        self.current_index = -3
    
    def __iter__(self):
        return self

    def __next__(self):
        self.current_index += 3
        if self.current_index < len(self.items):
            return self.items[self.current_index:self.current_index + 3]
        raise StopIteration

if __name__ == "__main__":
    with open("input", "r") as f:
        print(get_total_priority(f))
    with open("input", "r") as f:
        print(get_total_badge_priority(f.readlines()))
