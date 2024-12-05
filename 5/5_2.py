with open('input.txt', 'r') as file:
    lines = [line.strip() for line in file.readlines()]
    R = []
    P = []
    for line in lines:
        if "|" in line:
            a, b = line.split("|")
            R.append([int(a),int(b)])
        if "," in line:
            P.append([int(x) for x in line.split(",")])
    s = 0
    NV = []
    for p in P:
        T = []
        is_valid = True
        for N in p:
            for r in R:
                if r[0] == N and r[1] in T:
                    is_valid = False
                    break
            if not is_valid:
                break
            T.append(N)
        if not is_valid:
            NV.append(p)
    
    for p in NV:
        solved = False
        while not solved:
            solved = True
            for r in R:
                if r[0] in p and r[1] in p and p.index(r[0]) > p.index(r[1]):
                    i = p.index(r[0])
                    j = p.index(r[1])
                    p[i], p[j] = p[j], p[i]
                    solved = False
            if solved:
                s += p[len(p)//2]
    print(s)