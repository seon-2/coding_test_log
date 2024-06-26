from sys import stdin as s

number_of_trees, target = map(int, s.readline().strip().split())
trees = list(map(int, s.readline().split()))


# 가져갈 수 있는 나무 길이 구하기
def get_length_of_trees(length):
    total_length = 0
    for tree in trees:
        if tree > length:
            total_length += (tree - length) # 누적합
    return total_length


# 이분 탐색으로 더 작게 자를지 크게 자를지 결정 (이분탐색)
def longer_or_shorter(low, high):
    result = 0
    while low <= high:
        mid = (low + high) // 2
        length = get_length_of_trees(mid)

        if length >= target: # 타겟보다 더 많은 나무가 만들어짐 -> 더 크게 잘라보기 = 오른쪽 확인
            result = mid
            low = mid + 1
        else: # 타겟보다 더 적은 나무가 만들어짐 -> 더 많이(작게) 잘라야 함 = 왼쪽 확인
            high = mid - 1

    return result


print(longer_or_shorter(0, max(trees) - 1))