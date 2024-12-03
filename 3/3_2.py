import re

with open('input.txt', 'r') as file:
    input = file.read()

    do_pattern = r"do\(\)"
    dont_pattern = r"don't\(\)"

    do_matches = re.finditer(do_pattern, input)
    dont_matches = re.finditer(dont_pattern, input)

    do_indexes = [x.start() for x in do_matches]
    dont_indexes = [x.start() for x in dont_matches]

    do_indexes.append(0)

    mul_pattern = r"mul\(\d{1,3},\d{1,3}\)"
    mul_matches = re.finditer(mul_pattern, input)

    sum = 0

    for match in mul_matches:
        mul_start = match.start()
        largest_do = 0
        largest_dont = 0

        for do_index in do_indexes:
            if do_index < mul_start and do_index > largest_do:
                largest_do = do_index

        for dont_index in dont_indexes:
            if dont_index < mul_start and dont_index > largest_dont:
                largest_dont = dont_index

        if largest_do >= largest_dont:
            sum += eval(match.group().replace("mul(", "").replace(")", "").replace(",", "*"))
    print(sum)