strArr = [["there","are","no","a","ds"]]

def solution(strArr):
    answer = []
    for i in range(len(strArr)):
        if "ad" in strArr[i]:
            continue
        else:
            answer.append(strArr[i])
    return answer
print(solution(strArr))