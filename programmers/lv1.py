s = "one4seveneight"
num_list = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}

def solution(s):
    for k,v in num_list.items():
        if k in s:
            s = s.replace(k, v)
    return int(s)

print(solution((s)))