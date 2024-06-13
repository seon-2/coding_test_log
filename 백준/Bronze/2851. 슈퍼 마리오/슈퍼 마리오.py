mushrooms = [int(input().strip()) for _ in range(10)]
answer = 0

for i in range(1, 10):
    mushrooms[i] += mushrooms[i - 1]
    if mushrooms[i] == 100:
        answer = 100
        break
    elif mushrooms[i] > 100:
        # 더 가까운 것
        if mushrooms[i]-100 <= 100 - mushrooms[i-1]:
            answer = mushrooms[i]
        else:
            answer = mushrooms[i-1]
        break
else:
    answer = mushrooms[-1]
    
print(answer)
