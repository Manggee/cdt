numLog = [0, 1, 0, 10, 0, 1, 0, 10, 0, -1, -2, -1]

# 0에서 시작해서 조작한 결과가 numLog임 -> 어떤 알파벳에 의해 저런 결과가 나왔는지 출력하면 된다.

def solution(numLog):
    result = ""
    for i in range(1, len(numLog)):
        dif = numLog[i] - numLog[i - 1]
        if dif == 1:
            result += "w"
        elif dif == -1:
            result += "s"
        elif dif == 10:
            result += "d"
        elif dif == -10:
            result += "a"
    return result
print(solution(numLog))

# 좀 더 생각해야할 점: 차이점을 구하는 부분에서 [i + 1]에서 [i]를 빼면 안되는 이유
# range를 돌릴 떄 i가 3이 마지막이라고 치면 i + 1은 미래의 숫자를 기반으로 계산하기에 숫자가 존재하지 않아 인덱스 에러가 발생한다.
