# 공백으로 구분된 단어 개수 찾기
# 양 끝 공백 없애고 split

str = input()
print(len(str.strip().split()))