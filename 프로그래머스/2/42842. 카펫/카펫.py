# getDivisior 함수 개선

def solution(brown, yellow):
    
    def getAnswer(w, h):
        if 2 * (w+h) - 4 == brown:
            return True
        else:
            return False
        
    def getDivisior(n):
        divisors = []
        for i in range(1, int(n**0.5) + 1):
            if n % i == 0:
                divisors.append((n // i, i))
        return divisors

    d_list = getDivisior(brown+yellow)
    
    print(d_list)
    
    for d in d_list:
        if getAnswer(d[0], d[1]):
            return d

