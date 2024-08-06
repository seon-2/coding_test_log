def solution(word):
    dic = []
    
    def dfs(current_word, length):
        if len(current_word) == length:
            dic.append(current_word)
            return
        
        for char in ['A', 'E', 'I', 'O', 'U']:
            dfs(current_word + char, length)
    
    for i in range(1, 6):
        dfs("", i)
    
    return sorted(dic).index(word) + 1