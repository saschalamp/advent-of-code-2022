class SignalIterator:
    def __init__(self, stream, n):
        self.stream = stream
        self.n = n
        self.index = -1
    
    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index + self.n <= len(self.stream):
            return self.stream[self.index:self.index+self.n]
        raise StopIteration

def is_marker(sequence):
    d = set({})
    for c in sequence:
        d.add(c)
    return len(d) == len(sequence)

def find_marker(stream, n):
    marker = n
    for sequence in SignalIterator(stream, n):
        if is_marker(sequence):
            return marker
        marker += 1

if __name__ == "__main__":
    with open("input", "r") as f:
        stream = f.readlines()[0][:-1]
        print(find_marker(stream, 4))
        print(find_marker(stream, 14))
