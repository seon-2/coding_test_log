import sys

# 입력 받기
input_data = sys.stdin.read().split("\n")
N = int(input_data[0])
road_len = list(map(int, input_data[1].split()))
oil_price = list(map(int, input_data[2].split()))

# 초기화
cur_price = oil_price[0]
cost = 0

# 주유소 최적 경로 탐색
for i in range(N - 1):
    # 일단 현재 주유소에서 다음 도시까지 가야 함
    cost += cur_price * road_len[i]

    # 다음 주유소 가격이 더 싸다면, 다음 주유소에서 기름 충전
    if cur_price > oil_price[i + 1]:
        cur_price = oil_price[i + 1]

print(cost)