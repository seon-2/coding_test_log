import sys

read = sys.stdin.readline

n = int(read())
switches = list(map(int, read().strip().split()))
students = int(read())
instructions = [tuple(map(int, input().strip().split())) for _ in range(students)]

def toggle_switches(switches, gender, num):
    n = len(switches)
    if gender == 1:  # 남학생인 경우
        for i in range(num - 1, n, num):
            switches[i] = 1 - switches[i]
    else:  # 여학생인 경우
        num -= 1  # 인덱스로 변환 
        start = num
        end = num
        while start > 0 and end < n - 1 and switches[start - 1] == switches[end + 1]:
            start -= 1
            end += 1
        for i in range(start, end + 1):
            switches[i] = 1 - switches[i]

for gender, num in instructions:
    toggle_switches(switches, gender, num)

for i in range(0, len(switches), 20):
    print(*switches[i:i+20])
