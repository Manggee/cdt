arr = [[50,170],[70,160],[80,185]]

def solution(arr):
    for j in range(1,len(arr)):
        for i in range(j-1, -1, -1):
            if arr[i][0]+arr[i][1] > arr[i+1][0]+arr[i+1][1]:
                arr[i],arr[i+1] = arr[i+1],arr[i]
    return arr


print(solution(arr))