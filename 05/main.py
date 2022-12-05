from collections import deque
import re

def generate_stacks(input):
    stacks = []
    for row in input[:-1]:
        stack_index = 0
        row_index = 1
        while row_index < len(row):
            if len(stacks) < stack_index + 1:
                stacks.append(deque([]))
            crate = row[row_index].strip()
            if crate:
                stacks[stack_index].appendleft(crate)
            stack_index += 1
            row_index += 4
    return stacks

def move_crate(stacks, source, target):
    crate = stacks[source - 1].pop()
    stacks[target - 1].append(crate)

def move_multiple_crates(stacks, n, source, target):
    for _ in range(n):
        move_crate(stacks, source, target)

def move_multiple_crates_in_order(stacks, n, source, target):
    crates = []
    for _ in range(n):
        crates.insert(0, stacks[source - 1].pop())
    for crate in crates:
        stacks[target - 1].append(crate)

def determine_message(stacks):
    return "".join([stack[-1] for stack in stacks])

def translate_step(step):
    result = re.search(r"move (\d+) from (\d+) to (\d+)", step)
    return int(result.group(1)), int(result.group(2)), int(result.group(3))

def solve_puzzle(input):
    split = 0
    for i in input:
        split += 1
        if len(i) == 0:
            break
    stacks = generate_stacks(input[:split-1])
    for step in input[split:]:
        n, source, target = translate_step(step)
        move_multiple_crates(stacks, n, source, target)
    return determine_message(stacks)

def solve_puzzle_2(input):
    split = 0
    for i in input:
        split += 1
        if len(i) == 0:
            break
    stacks = generate_stacks(input[:split-1])
    for step in input[split:]:
        n, source, target = translate_step(step)
        move_multiple_crates_in_order(stacks, n, source, target)
    return determine_message(stacks)

if __name__ == "__main__":
    with open("input", "r") as f:
        print(solve_puzzle([line[:-1] for line in f.readlines()]))
    with open("input", "r") as f:
        print(solve_puzzle_2([line[:-1] for line in f.readlines()]))
