order = ["cafelatte", "americanoice", "hotcafelatte", "anything"]

# 1번째 방법
def solution(order):
    cost = 0
    for i in range(len(order)):
        if order[i] == "anything":
            cost += 4500
        elif "americano" in order[i]:
            cost += 4500
        elif "cafelatte" in order[i]:
            cost += 5000
    return cost
print(solution(order))

# 2번째 방법
def solution(order):
    cost = 0
    for i in range(len(order)):
        if "cafelatte" in order[i]:
            cost += 5000
        else:
            cost += 4500
    return cost
print(solution(order))
