directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]

with open('input.txt', 'r') as f:
    lines = [list(line) for line in f.read().splitlines()]
    current_position = ()
    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            if c == "^":
                current_position = [i, j]
    
    current_direction = 0
    end = False

    row_len = len(lines[0])
    col_len = len(lines)
    num_test = 0
    while not end:
        lines[current_position[0]][current_position[1]] = "X"
        i, j = [a + b for a, b in zip(current_position, directions[current_direction])]

        if 0 > i or i >= row_len or 0 > j or j >= col_len:
            end = True
            continue
        
        if lines[i][j] == "#":
            current_direction = (current_direction + 1) % len(directions)
            print(current_direction)
        if lines[i][j] == "." or lines[i][j] == "X":
            current_position = [i, j]
    x = 0
    for line in lines:
        print(line)
        for c in line:
            if c == "X":
                x += 1
    print(x) 

        


        
