with open('input.txt', 'r') as file:
    lines = file.readlines()
    A = []
    B = []
    for line in lines:
        numbers = line.split()
        A.append(int(numbers[0]))
        B.append(int(numbers[1]))

    sum = 0
    while A and B:
        minA = min(A)
        minB = min(B)
        distance = abs(minA - minB)
        sum += distance
        A.remove(minA)
        B.remove(minB)
    
    print(sum)