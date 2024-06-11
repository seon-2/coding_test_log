import heapq
import sys
input = sys.stdin.read

def get_min_cost(chapter_list):
    cost = 0
    heapq.heapify(chapter_list)
    while len(chapter_list) > 1:
        temp = heapq.heappop(chapter_list) + heapq.heappop(chapter_list)
        cost += temp
        heapq.heappush(chapter_list, temp)
    return cost

def main():
    data = input().split()
    index = 0
    test_case_num = int(data[index])
    index += 1
    results = []

    for _ in range(test_case_num):
        chapter_num = int(data[index])
        index += 1
        chapter_list = list(map(int, data[index:index + chapter_num]))
        index += chapter_num
        results.append(get_min_cost(chapter_list))

    print("\n".join(map(str, results)))

if __name__ == "__main__":
    main()
