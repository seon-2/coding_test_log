# 피보나치 수열 실행횟수 출력하기
# 리스트에 값 저장하는 방식 + 해당 줄이 불릴 때 카운트하기
n = int(input())

def fibo(n):
    f = [[1, 0] for i in range(41)]
    for i in range(3, n+1):
        f[i][0] = (f[i-1][0] + f[i-2][0])
        f[0][1] += 1
        f[i][1] = f[0][1]
    return f[n]

print(*fibo(n))