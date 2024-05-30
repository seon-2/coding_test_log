def solution(numbers, target):
    def dfs(index, sum_nums):
        if index == len(numbers):
            if sum_nums == target:
                return 1
            else:
                return 0
        else:
            # 현재 인덱스의 숫자를 더하거나 빼는 두 가지 경우 모두 탐색
            return dfs(index + 1, sum_nums + numbers[index]) + dfs(index + 1, sum_nums - numbers[index])

    return dfs(0, 0)
