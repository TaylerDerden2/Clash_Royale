import Налаштування

text_map = [
    ".....1111111111",
    "1.............1",
    "1.........1...1",
    "1............11",
    "1.............1",
    "111111111111111"
]

world_map = set()
for j, row in enumerate(text_map):
    for i, char in enumerate(row):
        if char != ".":
            world_map.add((i,j))