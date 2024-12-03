reports = []    
with open("input.txt") as file:
    for line in file:
        values = line.split(" ")
        values = [int(value) for value in values]
        reports.append(values)

def is_safe(report, changed = False, part_two = False):
    should_be_increasing = True if report[0] < report[1] else False
    for i in range(1, len(report)):
        is_increasing = report[i] > report[i - 1]
        in_range = 1 <= abs(report[i] - report[i - 1]) <= 3
        if should_be_increasing != is_increasing or not in_range:
            if changed or not part_two:
                return False
            safe_with_tolerate = False
            for i in range(len(report)):
                copy = report.copy()
                copy.pop(i)
                if is_safe(copy, True):
                    safe_with_tolerate = True
            return safe_with_tolerate
    return True

safe = 0
for report in reports:
    if is_safe(report):
        safe += 1
print(safe)

safe = 0
for report in reports:
    if is_safe(report, part_two = True):
        safe += 1
        
print(safe)