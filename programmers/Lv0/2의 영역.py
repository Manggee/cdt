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



# 2의 영역 복습

# 1. 2의 존재 여부 확인:
# 먼저 배열에 2가 전혀 없는지 확인해 보세요. 2가 없다면 바로 [-1]을 반환합니다.
# 2. 2의 첫 등장과 마지막 등장 찾기:
# 배열에 2가 있다면, 2가 처음으로 나타나는 인덱스와 마지막으로 나타나는 인덱스를 찾습니다.
# 3. 부분 배열 슬라이싱:
# 찾은 인덱스를 이용해 그 사이에 있는 모든 요소(처음과 마지막 포함)를 슬라이싱하면, 이것이 모든 2를 포함하는 가장 작은 연속된 부분 배열이 됩니다.

arr = [1,2,1,4,5,2,9]

def solution(arr):
    if not 2 in arr:
        return -1
    else:
        # 인덱스 찾기
        first = arr.index(2)
        last = max(i for i, x in enumerate(arr) if x == 2) # i는 인덱스, x는 값
        # 부분 배열 슬라이싱
        return arr[first:last+1]
print(solution(arr))


arr = [1,2,1,4,5,2,9]
g = min(i for i, x in enumerate(arr) if x ==2)
print(g)