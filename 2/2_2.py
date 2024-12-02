def is_list_valid(list):
    valid = True
    ascending = False
    if list[0] < list[1]:
        ascending = True
    for i in range(len(list) - 1):
        if ascending:
            difference = list[i + 1] - list[i]
        else:
            difference = list[i] - list[i + 1]
        if difference > 3 or difference <= 0:
            valid = False
    return valid


with open('input.txt', 'r') as file:
    lines = file.readlines()
    sum = 0
    for line in lines:
        A = [int(x) for x in line.split(" ")]
        if is_list_valid(A):
            sum += 1
            continue
        for i, number in enumerate(A):
            B = A[:i] + A[i+1:]
            if is_list_valid(B):
                sum += 1
                break
    print(sum)