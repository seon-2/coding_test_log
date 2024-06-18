from collections import defaultdict

def solution(N, students):
    photo_frames = []
    recommend_counts = defaultdict(int)
    recommend_times = defaultdict(int)

    for idx, student in enumerate(students, start=1):
        # 1. 이미 사진틀에 있는 경우, 추천 횟수만 증가
        if student in photo_frames:
            recommend_counts[student] += 1
        # 2. 사진틀에 빈 공간이 있는 경우, 추가
        elif len(photo_frames) < N:
            photo_frames.append(student)
            recommend_counts[student] = 1
            recommend_times[student] = idx
        # 3. 사진틀에 빈 공간이 없는 경우, 최소 추천 횟수 및 최오래된 학생 사진 제거 후 추가
        else:
            min_count = min(recommend_counts.values())
            min_students = [s for s, c in recommend_counts.items() if c == min_count]
            oldest_student = min(min_students, key=lambda x: recommend_times[x])

            photo_frames.remove(oldest_student)
            del recommend_counts[oldest_student]
            del recommend_times[oldest_student]

            photo_frames.append(student)
            recommend_counts[student] = 1
            recommend_times[student] = idx

    return sorted(photo_frames)

# 입력 받기
N = int(input())  # 사진틀 개수
total_recommendations = int(input())  # 총 추천 횟수 (사용하지 않음)
students = list(map(int, input().split()))  # 추천 학생 번호 리스트

# 결과 출력
result = solution(N, students)
print(*result)