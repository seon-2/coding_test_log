# 9명의 키를 다 더한 다음에 뺄 2명을 고르자.
# target = sum - 100
# 9개 중 2개 뽑는 조합 리스트를 순회해서 합이 target과 같은 것 찾기.
# 해당하는 조합 난쟁이 집합에서 빼기

from sys import stdin as s
from itertools import combinations

dwarfs = set(int(s.readline()) for _ in range(9))
target = sum(dwarfs)-100
two_dwarfs = list(combinations(dwarfs, 2))

for dwarf1, dwarf2 in two_dwarfs:
    if dwarf1 + dwarf2 == target:
        dwarfs.discard(dwarf1)
        dwarfs.discard(dwarf2)
        break

dwarfs_list = list(dwarfs)
dwarfs_list.sort()
print("\n".join(map(str, dwarfs_list)))