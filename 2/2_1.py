with open('input.txt', 'r') as file:
    lines = file.readlines()
    sum = 0
    for line in lines:
        A = [int(x) for x in line.split()]
        ascending = False
        valid = True

        if A[0] < A[1]:
            ascending = True

        for i in range(len(A) - 1):
            if ascending:
                difference = A[i + 1] - A[i]
            else:
                difference = A[i] - A[i + 1]
            if difference > 3 or difference <= 0:
                valid = False
        
        if valid:
            sum += 1
    print(sum)