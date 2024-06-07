# 1. 입학년도 % 100 오름차순
# 2. 문제 많이 푼 순서대로 성씨 알파벳

from sys import stdin as s

year_list = []
solved_list = []

# 입력
for _ in range(3):
    solved, year, name = map(str, s.readline().split())
    year_list.append(int(year) % 100)
    solved_list.append([int(solved), name[0]])


def get_team_name_by_year(year_list):
    return "".join(map(str, sorted(year_list)))


def get_team_name_by_solved(solved_list):
    solved_list.sort(key=lambda x: -x[0])
    team_name = ""
    for i in range(3):
        team_name += solved_list[i][1]
    return team_name


print(get_team_name_by_year(year_list))
print(get_team_name_by_solved(solved_list))