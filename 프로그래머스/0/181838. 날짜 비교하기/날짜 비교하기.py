def solution(date1, date2):
    d1 = [int(digit) for part in date1 for digit in f"{part:02d}"]
    d2 = [int(digit) for part in date2 for digit in f"{part:02d}"]

    print(f"d1: {d1}")
    print(f"d2: {d2}")
    print("****************************")

    if d1[0] < d2[0]: print(f"d1[0]: {d1[0]}가 d2[0]: {d2[0]}보다 작습니다."); return 1
    elif d1[0] > d2[0]: print(f"d1[0]: {d1[0]}가 d2[0]: {d2[0]}보다 큽니다."); return 0

    print(f"d1[0]: {d1[0]}가 d2[0]: {d2[0]}와 같습니다.")
    

    if d1[1] < d2[1]: print(f"d1[1]: {d1[1]}가 d2[1]: {d2[1]}보다 작습니다."); return 1
    elif d1[1] > d2[1]: print(f"d1[1]: {d1[1]}가 d2[1]: {d2[1]}보다 큽니다."); return 0

    print(f"d1[1]: {d1[1]}가 d2[1]: {d2[1]}와 같습니다.")

    
    if d1[2] < d2[2]: print(f"d1[2]: {d1[2]}가 d2[2]: {d2[2]}보다 작습니다."); return 1
    elif d1[2] > d2[2]: print(f"d1[2]: {d1[2]}가 d2[2]: {d2[2]}보다 큽니다."); return 0

    print(f"d1[2]: {d1[2]}가 d2[2]: {d2[2]}와 같습니다.")
    

    if d1[3] < d2[3]: print(f"d1[3]: {d1[3]}가 d2[3]: {d2[3]}보다 작습니다."); return 1
    elif d1[3] > d2[3]: print(f"d1[3]: {d1[3]}가 d2[3]: {d2[3]}보다 큽니다."); return 0

    print(f"d1[3]: {d1[3]}가 d2[3]: {d2[3]}와 같습니다.")
    

    if d1[4] < d2[4]: print(f"d1[4]: {d1[4]}가 d2[4]: {d2[4]}보다 작습니다."); return 1
    elif d1[4] > d2[4]: print(f"d1[4]: {d1[4]}가 d2[4]: {d2[4]}보다 큽니다."); return 0

    print(f"d1[4]: {d1[4]}가 d2[4]: {d2[4]}와 같습니다.")
    

    if d1[5] < d2[5]: print(f"d1[5]: {d1[5]}가 d2[5]: {d2[5]}보다 작습니다."); return 1
    elif d1[5] > d2[5]: print(f"d1[5]: {d1[5]}가 d2[5]: {d2[5]}보다 큽니다."); return 0

    print(f"d1[5]: {d1[5]}가 d2[5]: {d2[5]}와 같습니다.")
    

    if d1[6] < d2[6]: print(f"{d1[6]}가 d2[6]: {d2[6]}보다 작습니다."); return 1
    elif d1[6] > d2[6]: print(f"d1[6]: {d1[6]}가 d2[6]: {d2[6]}보다 큽니다."); return 0

    print(f"d1[6]: {d1[6]}가 d2[6]: {d2[6]}와 같습니다.")
    

    if d1[7] < d2[7]: print(f"d1[7]: {d1[7]}가 d2[7]: {d2[7]}보다 작습니다."); return 1
    elif d1[7] > d2[7]: print(f"d1[7]: {d1[7]}가 d2[7]: {d2[7]}보다 큽니다."); return 0
    
    print(f"d1[7]: {d1[7]}가 d2[7]: {d2[7]}와 같습니다.")
    
    print("****************************")
    print("원래는 코드를 단 한 줄로 작성할 수 있습니다.")
    print("그 코드는 다음과 같습니다.")
    print("return int(date1 < date2)")
    print("코드 설명")
    print("파이썬에서는 튜플 비교가 가능하므로")
    print("날짜를 각 요소별로 비교하여 date1이 date2보다 이전이면 True를 반환합니다.")
    print("int() 함수는 True를 1로, False를 0으로 변환합니다.")
    print("끝-!")
    
    return 0