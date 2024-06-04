import sys
# sys.stdin = open("input.txt","rt")

data = sys.stdin.readline().strip().split()
ip = data[0]

if "::" in ip:
    parts = ip.split("::")
    left = parts[0].split(":") if parts[0] else []
    right = parts[1].split(":") if parts[1] else []

    # 생략된 그룹의 수 계산
    missing_groups = 8 - (len(left) + len(right))
    middle = ["0000"] * missing_groups

    ip_list = left + middle + right
else:
    ip_list = ip.split(":")

for i in range(len(ip_list)):
    ip_list[i] = ip_list[i].zfill(4)


print(":".join(ip_list))
