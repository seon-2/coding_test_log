from sys import stdin as s

N = int(s.readline().strip())
budgets = sorted(list(map(int, s.readline().strip().split())))
total = int(s.readline().strip())

high = budgets[-1]
low = 1
answer = 0

while low <= high:
    mid = (high + low) // 2
    new_budgets = budgets[:] # 깊은 복사
    # 초과하는 금액 상한액으로 바꾸기
    for i in range(N):
        if budgets[i] > mid:
            new_budgets[i] = mid

    if sum(new_budgets) > total:
        high = mid - 1
    else:
        answer = mid
        low = mid + 1


print(answer)