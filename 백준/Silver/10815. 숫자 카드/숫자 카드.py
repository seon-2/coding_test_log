# 8번 : 숫자카드
# 상근이가 가진 숫자카드, 중복X
# 알고싶은 숫자들 -> 있으면 1, 없으면 0
# 범위가 커서 시간복잡도가 O(N) 보다 작아야겠다.

from sys import stdin as s
from collections import Counter, defaultdict

N = int(s.readline())
number_cards = s.readline().strip().split()
M = int(s.readline())
numbers = list(map(int, s.readline().strip().split()))

card_dict = Counter(map(int, number_cards))
number_dict = defaultdict(int)

for number in numbers:
    number_dict[number] = card_dict[number]

print(*number_dict.values())