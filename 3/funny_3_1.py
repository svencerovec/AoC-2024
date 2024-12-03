import re; print(sum([eval(match.replace("mul(", "").replace(")", "").replace(",", "*")) for match in re.findall(r"mul\(\d{1,3},\d{1,3}\)", "".join(open('input.txt', 'r').readlines()))]))
