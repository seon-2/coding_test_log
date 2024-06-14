def cal_generator(n):
    result = n
    for digit in str(n):
        result += int(digit)
    return result

selfnumbers = set(range(1, 10001))
generators = set()

for i in range(1, 10001):
    gen = cal_generator(i)
    if gen <= 10000:
        generators.add(gen)

selfnumbers -= generators

print("\n".join(map(str, sorted(selfnumbers))))