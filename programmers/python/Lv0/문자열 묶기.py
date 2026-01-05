strArr = ["a","bc","d","efg","hi"]

def solution(strArr):
    from collections import Counter
    lengths = [len(s) for s in strArr]
    length_counts = Counter(lengths)
    return max(length_counts.values())
print(solution(strArr))