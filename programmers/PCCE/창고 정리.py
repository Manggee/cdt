storage = ["pencil", "pencil", "pencil", "book"]
num = [2,4,3,1]

def solution(storage, num):
    clean_storage = []
    clean_num = []
    for i in range(len(storage)): # 0,1,2,3
        if storage[i] in clean_storage:
            pos = clean_storage.index(storage[i])
            clean_num[pos] += num[i]
        else:
            clean_storage.append(storage[i]) # num에서 storage로 수정
            clean_num.append(num[i])

    # 아래 코드에는 틀린 부분이 없습니다.

    max_num = max(clean_num)
    # clean_num list에서 9의 위치는 0번째이므로 clean_storage[0]이 되고 answer = "pencil"이 된다.
    answer = clean_storage[clean_num.index(max_num)]
    return answer
print(solution(storage, num))

# 아직 못 풀었다 내일 꼭 하도록