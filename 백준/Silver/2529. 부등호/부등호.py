def solve(k, signs):
    def dfs(idx, current, is_max):
        if idx == k + 1:
            return ''.join(map(str, current))

        range_to_check = range(9, -1, -1) if is_max else range(10)
        for num in range_to_check:
            if num not in current:
                if idx == 0 or eval(f"{current[-1]} {signs[idx - 1]} {num}"):
                    result = dfs(idx + 1, current + [num], is_max)
                    if result:
                        return result
        return None

    max_result = dfs(0, [], True)
    min_result = dfs(0, [], False)

    return max_result, min_result


k = int(input())
signs = list(map(str, input().split(' ')))
max_num, min_num = solve(k, signs)

print(max_num)
print(min_num)