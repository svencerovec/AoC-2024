directions = [
    [[1, 1],[-1, -1]],
    [[1, -1],[-1, 1]]
]

with open('input.txt', 'r') as file:
    CWP = [line.strip() for line in file.readlines()]
    xmas_count = 0

    num_rows = len(CWP)
    num_cols = len(CWP[0])

    for r, R in enumerate(CWP):
        for c, C in enumerate(R):
            if C == 'A':
                is_xmas = True
                for d1, d2 in directions:
                    r1, c1 = r + d1[0], c + d1[1]
                    r2, c2 = r + d2[0], c + d2[1]
                    if not(0 <= r1 < num_rows and 0 <= c1 < num_cols and 0 <= r2 < num_rows and 0 <= c2 < num_cols and
                        ((CWP[r1][c1] == 'M' and CWP[r2][c2] == 'S') or (CWP[r1][c1] == 'S' and CWP[r2][c2] == 'M'))):
                        is_xmas = False
                        break
                if is_xmas:
                    xmas_count += 1
    print(xmas_count)