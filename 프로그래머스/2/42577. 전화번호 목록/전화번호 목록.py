def solution(phone_book):
    hash_set = set(phone_book)
    
    for phone_number in phone_book:
        for i in range(1, len(phone_number)):
            prefix = phone_number[:i]
            if prefix in hash_set and prefix != phone_number:
                return False
    
    return True