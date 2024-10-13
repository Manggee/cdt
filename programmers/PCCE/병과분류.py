# code = input()
code = "dry_eye"

last_four_words = code[-4:]  # 이 부분 검색해서 공부하기

if last_four_words == "_eye":
    print("Ophthalmologyc")
elif last_four_words == "head":
    print("Neurosurgery")
elif last_four_words == "infl":
    print("Orthopedics")
elif last_four_words == "skin":
    print("Dermatology")
else:
    print("direct recommendation")
