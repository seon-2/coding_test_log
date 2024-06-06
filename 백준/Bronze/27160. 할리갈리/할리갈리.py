from sys import stdin
from collections import defaultdict

# 과일 개수 세기
def count_fruits():
    fruit_counts = defaultdict(int)
    for _ in range(int(stdin.readline())):
        fruit, count = stdin.readline().strip().split()
        fruit_counts[fruit] += int(count)
    return fruit_counts

# 과일 개수 중 5인 것 확인
def has_enough_fruits(fruit_counts):
    return any(count == 5 for count in fruit_counts.values())

def main():
    fruit_counts = count_fruits()
    print("YES" if has_enough_fruits(fruit_counts) else "NO")

if __name__ == "__main__":
    main()