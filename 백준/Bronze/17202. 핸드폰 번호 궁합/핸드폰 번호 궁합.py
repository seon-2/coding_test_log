from sys import stdin as s

number1 = s.readline().strip()
number2 = s.readline().strip()

# 두 번호를 번갈아가며 하나씩 이어붙이기
combined_number = ""
for i in range(len(number1)):
    combined_number += number1[i] + number2[i]

# 계산 과정
result = [int(x) for x in combined_number]
while len(result) > 2:
    temp = []
    for i in range(len(result) - 1):
        digit_sum = result[i] + result[i + 1]
        temp.append(digit_sum % 10)
    result = temp

# 궁합률 출력
compatibility_rate = int(''.join(map(str, result)))
print(f"{compatibility_rate:02d}")