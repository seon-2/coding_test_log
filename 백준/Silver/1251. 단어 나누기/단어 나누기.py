word = input().strip()
new_words = []

for i in range(1, len(word)-1):
    for j in range(i+1, len(word)):
        new_words.append(word[:i][::-1] + word[i:j][::-1] + word[j:][::-1])

print(sorted(new_words)[0])
