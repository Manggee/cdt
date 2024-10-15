vec = [2,3,5]
mat = [[2,4],[3,8],[1,9]]
# [(2*2 + 3*3 + 5*1) , (2*4 + 3*8 + 5*9)] = [18,77]

def solutions(vec, mat):
    answer = []
    for i in range(len(mat[0])): # range(2)
        temp = 0
        for j in range(len(mat)): # range(3)
            temp += vec[j] * mat[j][i] # j가 0,1,2 다 돌아야 i에 다음 숫자가 들어옴
        answer.append(temp) # answer 라는 리스트에 첨부하기
    return answer
print(solutions(vec, mat))

