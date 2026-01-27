def solution(myStr):
    answer = []
    temp = ""
    for i in myStr:
        if i in ["a", "b", "c"]:
            if temp != "":
                answer.append(temp)
                temp = ""
            else:
                continue
        else:
            temp += i
    if temp != "":
        answer.append(temp)
    if answer == []:
        return ["EMPTY"]
    return answer

# myStr = "baconlettucetomato"
# myStr = "cabab"


# 더 깔끔한 방법
# def solution(myStr):
#     for i in "abc":
#         myStr = myStr.replace(i, " ")
#     ans = myStr.split()   # split()은 공백 여러 개를 자동으로 무시함
#     return ans if ans else ["EMPTY"]
# print(solution(myStr))