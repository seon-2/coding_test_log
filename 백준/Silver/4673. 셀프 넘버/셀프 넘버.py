numbers = [0] * 10001
for i in range(1, 10001):
    num = i
    divided = [j for j in str(i)]
    for k in divided:
        num += int(k)
    if num < 10001:
        numbers[num] = 1

results = []

for l in range(1, 10001):
    if numbers[l] == 0:
        results.append(l)

print("\n".join(map(str, results)))