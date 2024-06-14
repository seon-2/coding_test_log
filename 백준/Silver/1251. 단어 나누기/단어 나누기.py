word = input().strip()
divided_words = []
new_words = []
# 단어 세 부분으로 나누기
for i in range(1, len(word)-1):
    for j in range(i+1, len(word)):
        divided_words.append([word[:i], word[i:j], word[j:]])

# 단어 뒤집어서 합치기
for dw in divided_words:
    new_words.append(dw[0][::-1] + dw[1][::-1] + dw[2][::-1])

print(sorted(new_words)[0])