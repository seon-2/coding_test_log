# 노래의 첫 세 음 맞추기

import sys
# sys.stdin = open("input.txt", "rt")
data = sys.stdin.readline

N, M = map(int, data().split())
songs = [data().strip().split() for _ in range(N)]
quiz = [data().strip() for _ in range(M)]
song_dict = {}

for song in songs:
    T = int(song[0])
    S = song[1]
    song_dict[S] = " ".join(song[2:5])

answers = []
for q in quiz:
    count = list(song_dict.values()).count(q)
    if count > 1:
        answers.append('?')
    elif count == 1:
        answers.append([k for k, v in song_dict.items() if v == q])
    else:
        answers.append("!")

def print_results(answers):
    for answer in answers:
        if isinstance(answer, list):
            print(answer[0])
        else:
            print(answer)

print_results(answers)