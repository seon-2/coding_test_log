def solution(numbers):
    strings = [str(num) for num in numbers]
    strings.sort(key=lambda x: x * 3, reverse=True)
    answer = ''.join(strings)
    return '0' if answer[0] == '0' else answer