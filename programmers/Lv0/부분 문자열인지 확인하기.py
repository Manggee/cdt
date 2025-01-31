my_string = "banana"
targert = "ana"
def solution(my_string, target):
    answer = 0
    if target in my_string:
        return 1
    else:
        return 0
print(solution(my_string, targert))