arr = [1, 2, 1, 4, 5, 2, 9]
def solution(arr):
    answer = []
    arr.index(2)


arr = [1, 2, 1, 2, 1, 10, 2, 1]
locate = [i for i, v in enumerate(arr) if v == 2]
print(locate)
result = arr[locate[0]:locate[-1]+1] # end가 5인 경우 4까지만 출력되기에 1을 더해준다.
print(result)

# 생각하지 못한 부분
# locate의 인덱스가 두 개만 출력되는 경우라면 [0:1]로 해도 문제가 없으나 3개 이상 출력하는 경우 원하는 값을 end point로 설정할 수 없다.