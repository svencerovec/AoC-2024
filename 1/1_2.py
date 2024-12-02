with open('input.txt', 'r') as file:
    lines = file.readlines()
    A = []
    B = []
    for line in lines:
        numbers = line.split("   ")
        A.append(int(numbers[0]))
        B.append(int(numbers[1]))
    
    sum = 0
    for number in A:
        similarity = B.count(number)
        sum += number * similarity
    
    print(sum)
