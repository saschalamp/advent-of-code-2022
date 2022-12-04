def is_fully_contained(a, b):
    return a[0] >= b[0] and a[1] <= b[1]

def has_full_containment(a, b):
    return is_fully_contained(a, b) or is_fully_contained(b, a)

def as_tuple(input):
    return tuple(int(e) for e in input.split("-"))

def parse_tuple(input):
    t = input.split(",")
    return as_tuple(t[0]), as_tuple(t[1])

def describes_full_containment(input):
    a, b = parse_tuple(input)
    return has_full_containment(a, b)

def count_full_containments(input):
    return sum(1 for i in input if describes_full_containment(i))

def is_overlapping(a, b):
    return max(a[0], b[0]) <= min(a[1], b[1])

def describes_overlapping(input):
    a, b = parse_tuple(input)
    return is_overlapping(a, b)

def count_overlapping_pairs(input):
    return sum(1 for i in input if describes_overlapping(i))

if __name__ == "__main__":
    with open("input", "r") as f:
        print(count_full_containments(f.readlines()))
    with open("input", "r") as f:
        print(count_overlapping_pairs(f.readlines()))
