import re

with open('input3.txt') as f:
    data = f.read()

do_p = r"do\(\)"
dont_p = r"don't\(\)"
mul_p = r"mul\((\d+),(\d+)\)"

res = 0
enabled = True

for match in re.finditer(f"{do_p}|{dont_p}|{mul_p}", data):
    current_match = match.group(0)

    if re.match(do_p, current_match):
        enabled = True
    elif re.match(dont_p, current_match):
        enabled = False
    else:
        if enabled:
            first, second = int(match.groups()[0]), int(match.groups()[1])
            res += first * second

print(res)
