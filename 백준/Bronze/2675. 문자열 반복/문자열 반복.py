# 각 문자열의 문자를 R번씩 반복해서 새로운 문자열 출력
# 3 ABC 이면 AAABBBCCC

from sys import stdin as s

# s=open("input.txt","rt")

N = int(s.readline())
data = [s.readline().strip().split() for _ in range(N)]
answer = []

def repeat(R, string):
    r_str = ""
    for str in string:
        r_str = r_str + str * R

    return r_str

for d in data:
   answer.append(repeat(int(d[0]), d[1]))

print("\n".join(answer))

