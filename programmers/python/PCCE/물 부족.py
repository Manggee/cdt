storage = 5141
usage = 500
change = [10, -10, 10, -10, 10, -10, 10, -10, 10, -10]

def solution(storage, usage, change):
    total_usage = 0
    for i in range(len(change)): # range(10)
        # 사용량 * 변화량 / 100을 한 후에 더해주면 그 달의 사용량을 알 수 있다.
        usage += usage * change[i] /100
        total_usage += usage # 그 달의 사용량을 총 사용량에 더해주면 된다.
        if total_usage > storage:
            return i

    return -1
    # return i로 끝나지 않은 경우 어차피 for문을 빠져나옴. 그리고 그대로 아래로 내려와 -1을 출력함
print(solution(storage, usage, change))