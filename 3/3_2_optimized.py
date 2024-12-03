import re

def mul(a,b):
    return a * b

with open('input.txt', 'r') as file:
    input = file.read()
    pattern = r"do\(\)|don't\(\)|mul\(\d{1,3},\d{1,3}\)"
    matches = re.findall(pattern, input)
    sum = 0
    power_switch = 1
    for match in matches:
        if match == "do()":
            power_switch = 1
        if match == "don't()":
            power_switch = 0
        if match.startswith("mul") and power_switch == 1:
            sum += eval(match)
    print(sum)