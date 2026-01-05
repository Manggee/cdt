myString = "aaAA"
pat = "aaaaa"

def solution(myString, pat):
    sentence = myString.lower()
    pat = pat.lower()
    if pat in sentence:
        return 1
    else:
        return 0
print(solution(myString, pat))