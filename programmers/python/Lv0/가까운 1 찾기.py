arr = [1,1,1,1,0]
idx = 3

def solution(arr, idx):
    for i in range(idx, len(arr)):
        if arr[i] == 1:
            return i
    else:
        return -1

print(solution(arr, idx))
