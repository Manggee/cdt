myString = 'dxcccxaxb'

def solution(myString):
    # 'x'를 기준으로 문자열 분리 후 빈 문자열을 제거
    parts = [s for s in myString.split("x") if s != '']
    # 사전순으로 정렬하여 반환
    return sorted(parts)

print(solution(myString))

# sorted() : 리스트를 정렬된 새로운 리스트로 반환
# .split('') : '' 안에 있는 값을 기준으로 쪼갬

# 모르는 개념이 많았다. 추후에 다시 풀어볼 것