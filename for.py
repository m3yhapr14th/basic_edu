#!/usr/bin/python3
# 반복문(for)
print("대기번호: 1")
print("대기번호: 2")
print("대기번호: 3")
print("대기번호: 4")

for waitnum in range(1, 6): # 1, 2, 3, 4, 5
    print("대기번호: {0}".format(waitnum))

starbucks = ["아이언맨", "토르", "그루트"]
for customer in starbucks:
    print("{0}님, 커피가 준비되었습니다.".format(customer))