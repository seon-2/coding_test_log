# dfs 사용
from sys import stdin as s

n, m = map(int, s.readline().strip().split())

answer = []
temp = []

# 중복 없이 DFS
def dfs():
    if len(temp) == m:
        answer.append(temp[:])
        return

    for i in range(1, n + 1):
        if all(v < i for v in temp):
            temp.append(i)  # temp에 요소 추가
            dfs()  # 하위 노드로 이동(재귀) 또는 길이 맞을 때마다 temp를 answer에 추가.
            temp.pop()  # 이전 노드로 복귀.

dfs()
print("\n".join(" ".join(map(str, v)) for v in answer))