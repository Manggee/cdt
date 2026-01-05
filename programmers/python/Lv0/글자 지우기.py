my_string = "apporoograpemmemprs"
indices = [1, 16, 6, 15, 0, 10, 11, 3]

# def solution(my_string, indices):
#     for i in range(len(my_string)):
#         if i in indices:
#             answer = my_string.replace(my_string[i], ' ')
#
#
# print(solution(my_string, indices))

# 오답:
# replace를 사용할 경우 my_string[i]에 해당하는 단어는 전부 공백으로 바꿔버린다.
# 예를 들어 my_string[i]가 a라면 a는 전부 공백으로 바뀐다.

def solution(my_string, indices):
    answer = ''
    for i in range(len(my_string)):
        if i not in indices:
            answer += my_string[i]
    return answer

print(solution(my_string, indices))

# indices에 해당하는 글자를 없애지 말고 반대로 indices에 들어가있지 않은 글자만 모은다고 생각하고 풀기