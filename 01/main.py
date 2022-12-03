import functools

def determine_most_calories(data):
    elves = []
    current_value = 0
    for i in data:
        i = i.rstrip()
        if len(i) == 0:
            elves.append(current_value)
            current_value = 0
        else:
            current_value += int(i)
    elves.append(current_value)
    return sorted(elves, reverse=True)[:3]

if __name__ == "__main__":
    with open("input", "r") as f:
        top_3 = determine_most_calories(f)
        print(top_3[0])
        print(sum(top_3))
