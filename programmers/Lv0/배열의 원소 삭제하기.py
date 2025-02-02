arr = [293, 1000, 395, 678, 94]
delete_list = [94, 777, 104, 1000, 1, 12]

def solution(arr, delete_list):
    for i in range(len(arr)-1):
        if arr[i] in delete_list:
            arr.pop(i)
    return arr
print(solution(arr, delete_list))
#  내가 생각한 방법의 문제점
# delete_list 안에 있는 원소를 arr 내에서 삭제해버리면 인덱스 순서가 꼬여서 다음 i를 건너뛰는 상황이 생긴다.

# 정답 1
def solution(arr, delete_list):
    return [x for x in arr if x not in delete_list]
print(solution(arr, delete_list))

# 정답 2
def solution(arr, delete_list):
    answer = []
    for i in delete_list:
        if i in arr:
            arr.remove(i)
    return arr