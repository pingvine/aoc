with open('input2.txt') as f:
    reports = [[int(num) for num in line.split()] for line in f.read().splitlines()]
    
def is_ascending_or_descending(row):
    return row == sorted(row) or row[::-1] == sorted(row)

def has_low_diff(row):
    return all(1<=abs(i-j)<=3 for i,j in zip(row[:-1],row[1:]))

def is_safe(row):
    return is_ascending_or_descending(row) and has_low_diff(row)

print(sum(is_safe(report) for report in reports))
print(sum(any(is_safe(report[:i]+report[i+1:]) for i in range(len(report))) for report in reports))