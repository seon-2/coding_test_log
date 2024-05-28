def solution(brown, yellow):
    
    def getAnswer(w, h):
        if 2 * (w+h) - 4 == brown:
            return True
        else:
            return False
        
    def getDivisior(n):
        d_list = []

        for i in range(1, int(n**(1/2)) + 1):
            temp = []
            if n % i == 0:
                if (i**2) != n:
                    temp.append(n // i)
                    temp.append(i)
                else:
                    temp.append(i)
                    temp.append(i)
                d_list.append(temp)

        return d_list

    d_list = getDivisior(brown+yellow)
    
    print(d_list)
    
    for d in d_list:
        if getAnswer(d[0], d[1]):
            return d


# b+y 가 w*h인지 찾기
# 카펫이 되는 경우가 뭘까
# 48의 약수는 (1, 48) (2, 24) (3, 16) (4, 12) (6, 8) 인데
# 무조건 1이 포함되어있으면 안되고, 2도 안되네. 갈색이 테두리여야 하니까.
# 테두리(b)의 개수는 2(w+h) - 4 : 모서리 제외
# 이런 조건을 만족하는 거 찾기
