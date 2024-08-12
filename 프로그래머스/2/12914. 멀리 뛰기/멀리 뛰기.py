def solution(n):
    if n == 1: 
        return 1
    else:    
        a, b = 1, 2
        for _ in range(3, n+1):
            a, b = b, (a + b) % 1234567
        return b

# f(n) = f(n-1) + f(n-2)

