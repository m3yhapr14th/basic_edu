print("Python", "Java", "JavaScript", sep=" vs ") # 값 사이 들어갈 값(구분자)
print("Python", "Java", "JavaScript", sep=", ") # 값 사이 들어갈 값(구분자)
print("Python", "Java", "JavaScript", sep=", ", end="?") # 해당 라인의 마지막 글자
print("무엇이 더 재밌을까요?")

# import sys
# print("Python", "Java", "JavaScript", file=sys.stdout) #표준 출력으로 문장이 찍힘
# print("Python", "Java", "JavaScript", file=sys.stderr) #표준 에러로 출력

# 시험 성적
scores = {"수학":0, "영어":50, "코딩": 100}
for subject, score in scores.items(): # 사전 item에 키: 값을 해당 변수로 정해줌
    #print(subject, score)
    print(subject.ljust(8), str(score).rjust(4), sep=":")

# 은행 대기순번표
# 001, 002, 003, ...

for num in range(1, 21):
    print("대기번호: " + str(num).zfill(3)) #Zero Fill 0을 채운다. 3개 공간 확보하고 값을 입력 후 나머지 공간을 0으로 채운다

answer = input("아무 값이나 입력하세요: ") # input으로 입력 값을 받으면 모두 str
print(type(answer))
print("입력하신 값은 " + answer + "입니다.")
