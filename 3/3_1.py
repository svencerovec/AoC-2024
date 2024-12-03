import re

with open('input.txt', 'r') as file:
    input = file.read()
    pattern = r"mul\(\d{1,3},\d{1,3}\)"
    matches = re.findall(pattern, input)
    sum = 0
    for match in matches:
        sum += eval(match.replace("mul(", "").replace(")", "").replace(",", "*"))
    print(sum)