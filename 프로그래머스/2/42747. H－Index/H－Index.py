def solution(citations):
    n = len(citations)
    citations.sort(reverse=True)
    
    for i, citation in enumerate(citations, 1):
        if citation < i:
            return i - 1
    return n