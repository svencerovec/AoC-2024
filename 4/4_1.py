directions = [
    [1, 0],
    [0, 1],
    [-1, 0],
    [0, -1],
    [1, 1],
    [-1,-1],
    [1,-1],
    [-1,1]
]

with open('input.txt', 'r') as file:
    CWP = [line.strip() for line in file.readlines()]

    xmas = ['X', 'M', 'A', 'S']
    xmas_count = 0

    num_rows = len(CWP)
    num_cols = len(CWP[0])
    len_xmas = len(xmas)

    for r, R in enumerate(CWP):
        for c, C in enumerate(R):
            if C == "X":
                for D in directions:
                    is_xmas = True
                    for i in range(len(xmas)):
                        r_step = r + i * D[0]
                        c_step = c + i * D[1]
                        if not(0 <= r_step < num_rows and 0 <= c_step < num_cols) or CWP[r_step][c_step] != xmas[i]:
                            is_xmas = False
                            break
                    if is_xmas:
                        xmas_count += 1
    print(xmas_count)