vec = [2,3,5]
mat = [2,4], [3,8], [1,9]

def solution(vec, mat):
    answer = []

    for i in range(len(mat[0])):
        temp = 0
        for j in range(len(mat)):
            temp += vec[j] * mat[j][i]
        answer.append(temp)
    return answer

print(solution(vec, mat))
