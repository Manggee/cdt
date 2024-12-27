todo_list = ["problemsolving", "practiceguitar", "swim", "studygraph"]
finished = [True, False, True, False]


def solution(todo_list, finished):
    result = []
    for i in range(len(todo_list)):
        if finished[i] == True:
            continue
        elif finished[i] == False:
            result.append(todo_list[i])
    return result
print(solution(todo_list, finished))

# todo_list = 해야 할 일
# finished[i] = true or false
# todo_list에서 아직 마치지 못한 일들을 순서대로 담은 문자열 배열 return 하기