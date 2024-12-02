left, right = [], []
with open("input.txt") as file:
    for line in file:
        values = line.split("   ");
        left.append(int(values[0]))
        right.append(int(values[1]))

left.sort()
right.sort()

total_distance = 0
for i in range(len(left)):
    total_distance += abs(left[i] - right[i])

similarity_score = 0
for num in left:
    similarity_score += num * right.count(num)

print("Total Distance: ", total_distance)
print("Similarity Score: ", similarity_score)