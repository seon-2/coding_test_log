def solution(n, times):
    answer = 0
    
    def find_min_time(low, high):
        while low <= high:
            mid = (high + low) // 2
            total_people = sum(mid // time for time in times)
            
            if total_people >= n: # 시간 늘리기
                high = mid - 1
            else:
                low = mid + 1
                
        return low
    
    answer = find_min_time(1, max(times)*n)
    
    return answer


# 최고로 많이 걸리면 6명을 2번 심사대에서 다 보는 60분이 걸림.
# 절반인 시간에는 몇 명을 볼 수 있을까?
# 1+60//2 = 30분; 1:4명, 2:3명 = 총 7명 => 더 많이 볼 수 있으니 시간을 줄여보자
# 1+30//2 = 15분; 1:2명, 2:1명 = 총 3명 => 6명보다 작으니 시간을 늘려보자
# 15+30//2 = 22분; 1:3명, 2:2명 = 총 5명 => 시간을 더 늘려보자
# 22+30//2 = 26분; 1:3명, 2:2명 = 총 5명 => 시간을 더 늘려보자
# 26+30//2 = 28분; 1:4명, 2:2명 = 총 6명 => 같다! 더 짧은 시간에 가능한가?
# 26+28//2 = 27분; 1:3명, 2:2명 = 총 5명 => 안되는군, 아까가 정답!