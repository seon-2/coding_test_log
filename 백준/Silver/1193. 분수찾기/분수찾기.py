# 지그재그로 된 규칙 찾기, X번째 분수는?
# 대각선 상에 있는 분수끼리는 분자 분모의 합이 같다.
# X번째 분수가 속한 행(분자와 분모의 합)을 찾으려면 삼각수를 이용한다. 1, 3, 6, 10, 15 ...
# X = 14일 때, 14보다 크거나 같은 최소 삼각수의 인덱스가 분자와 분모의 합이다. 여기서는 6
# 삼각수 값은 (1,5) 일까 (5,1)일까?
# 인덱스가 짝수이면 = 삼각수 값은 (1, 인덱스-1)이다.
# 1+삼각수-X 만큼이 분자이고 합-분자가 분모이다.
# (1+15-14, 6-분자)
# 인덱스가 홀수이면 삼각수 값은 (인덱스-1, 1)이다.
# (인덱스-분모, 1+삼각수-X)


from sys import stdin as s

X = int(input())

def find_max_triangle_number(n):
    start = 1
    end = 1
    sum = 0

    while sum < n:
        sum += end
        end += 1

    return sum, end

tri_num, tri_idx = find_max_triangle_number(X)
temp = 1+tri_num-X # 홀수 - 분자, 짝수 - 분모

if tri_idx % 2:
    answer = f'{tri_idx-temp}/{temp}'
else:
    answer = f'{temp}/{tri_idx-temp}'

print(answer)
