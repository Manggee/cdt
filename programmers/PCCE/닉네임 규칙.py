# nickname = "WORLDworld"
nickname = "G"

def solution(nickname):
    answer = ""
    for letter in nickname:
        if letter == "l":
            answer += "I"
        elif letter == "w":
            answer += "vv"
        elif letter == "W":
            answer += "VV"
        elif letter == "O":
            answer += "0"
        else:
            answer += letter
    if len(answer) < 3:
        answer += "o"*(4-len(answer))
    if len(answer) > 8:
        answer = answer[:8]
    return answer
print(solution(nickname))

# 4글자 ~ 8글자 이하
# l,w O,W 사용 불가
# 소문자 l을 대문자 I로 변경합니다
# 소문자 w를 두 개의 소문자 v, 즉 vv로 변경합니다.
# 대문자 W를 두 개의 대문자 V, 즉 VV로 변경합니다
# 대문자 O -> 0
# 길이가 4 미만이면 o 붙여서 4글자 될 때까지 채우기
# 길이가 8 초과일 경우 8번째 문자까지만 사용
