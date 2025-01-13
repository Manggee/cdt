arr = [3,2,4,1,3]
flag = [True, False, True, False, False]

def solution(arr, flag):
    X = []
    for i in range(len(arr)):
        if flag[i] == True:
            X.extend([arr[i]] * (arr[i] * 2)) # list.extend()는 리스트를 인자로 받아야하기에 숫자를 받을 시 에러가 남.
        else:
            X = X[:-arr[i]]
    return X
print(solution(arr, flag))

# extend 와 append 의 차이점
# append : 전달된 객체를 그대로 배열에 추가한다. [1,2,[3]]
# extend : 배열 끝에 여러 요소를 풀어서 추가합니다. [1,2,3]


