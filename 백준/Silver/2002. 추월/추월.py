import sys
# sys.stdin = open("input.txt","rt")

read = sys.stdin.readline

N = int(read())
in_seq = {}
out_seq = {}
for i in range(N):
    in_seq[read().strip()] = i

for i in range(N):
    out_seq[read().strip()] = i

cnt = 0
in_seq_list = []

for car_num, seq in out_seq.items():
    in_seq_list.append(in_seq[car_num])

for car_num, seq in out_seq.items():
    if in_seq_list[seq+1:] and in_seq[car_num] > min(in_seq_list[seq+1:]):
        cnt += 1
    # print(car_num, seq, in_seq[car_num])

# print(in_seq_list)
print(cnt)