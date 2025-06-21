q = 3
r = 1
code = "qjnwezgrpirldywt"

def solution(q, r, code):
    answer = ''
    for i in range(len(code)):
        if i % q == r:
            answer += code[i]
    return answer

print(solution(q, r, code))

# 오답 ✅
# for i in code:
#     if code.index(i) % q == r:
#         answer += i

# code.index(i)는 해당 문자가 처음 등장하는 인덱스를 반환한다.
# 따라서 code 안에 첫번째 글자 q가 두 번 등장한다면 인덱스는 둘 다 0으로 반환된다.