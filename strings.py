#!/usr/bin/python3

python = "Python is Amazing"
print(python.lower()) # 소문자
print(python.upper()) # 대문자
print(python[0].isupper()) # [0]번째 글자가 대문자냐?
print(len(python)) # 변수의 길이
print(python.replace("Python", "Java")) # a를 b로 대체

index = python.index("n") # 알파벳 n은 몇번째 (0부터)
print(index)
index = python.index("n", index + 1) # 1번째 알파벳 n을 찾은 이후 n은 몇번째
print(index)

print(python.find("Python")) # 글자 Python를 찾아라 (0: True, -1: False)
print(python.count("n")) # "n"은 몇개

# 문자열 포멧
print("나는 %d살입니다" % 3212) # 정수
print("나는 %s을 좋아해요" % "Apple") # 문자열
print("Apple은 %c로 시작해요" % "A") # Character
print("나는 %s색과 %s색을 좋아해요" % ("파란", "빨간"))

print("나는 {}살입니다." .format(20))
print("나는 {}색과 {}색을 좋아합니다" .format("빨간", "파란"))

print("나는 {0}색과 {1}색을 좋아합니다" .format("빨간", "파란"))
print("나는 {1}색과 {0}색을 좋아합니다" .format("빨간", "파란"))

print("나는 {age}살이며, {color}색을 좋아해요" .format(age = 3212, color="빨간"))

# v3.6 이상
age = 3212
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요")

# 탈출 문자 
# \n : 줄바꿈
print("백문이 불여일견\n백견이 불여일타")

# 저는 "nothing"입니다.
print("저는 \"nothing\"입니다.")

# \\ : 문장 내에서 \
print("C:\\Users\\nothing\\Desktop\\Workspace")

# \r : 커서를 맨 앞으로 이동 후 insert
print("Red Apple\rPine")

# \b : backspace
print("Redd\b Apple")

# \t : Tab
print("Red\tApple")
