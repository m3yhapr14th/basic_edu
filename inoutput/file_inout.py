# score_file = open("score.txt", "w", encoding="utf-8") # w: 쓰기, r: 읽기
# print("수학 : 0", file=score_file)
# print("영어 : 50", file=score_file)
# score_file.close()

# score_file = open("score.txt", "a", encoding="utf-8") # w: 쓰기, r: 읽기, a: 이미 있는 파일에 이어서(append)
# score_file.write("과학 : 80")
# score_file.write("\n코딩 : 100")
# score_file.close()

score_file = open("score.txt", "r", encoding="utf-8")
print(score_file.read())
score_file.close()

score_file = open("score.txt", "r", encoding="utf-8")
print(score_file.readline()) # 줄 별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
print(score_file.readline())
print(score_file.readline())
print(score_file.readline())
score_file.close()

score_file = open("score.txt", "r", encoding="utf-8")
print(score_file.readline(), end = "") # 줄 별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
print(score_file.readline(), end = "") # 줄 바꿈 없이
print(score_file.readline(), end = "")
print(score_file.readline(), end = "")
score_file.close()

# 라인 수 모를떄
score_file = open("score.txt", "r", encoding="utf-8")
while True:
    line = score_file.readline()
    if not line:
        break
    print(line, end="")
score_file.close()

score_file = open("score.txt", "r", encoding="utf-8")
lines = score_file.readlines() # list 형태로 저장
for line in lines:
    print(line, end="")
score_file.close()