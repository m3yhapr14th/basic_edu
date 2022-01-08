#!/usr/bin/python3

#당신의 학교에서는 파이썬 코딩 대회를 주최합니다.
#참석률을 높이기 위해 댓글 이벤트를 진행하기로 했습니다.
#댓글 작성자등 중에 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받게 됩니다.
#추첨 프로그램을 작성하시오

#조건1: 편의상 댓글은 20명이 작성하였고 아이디는 1~20이라고 가정
#조건2: 댓글 내용과 상관없이 무작위로 추첨하되 중복 불가
#조건3: random 모듈의 shuffle과 sample을 활용

#(출력 예제)
# -- 담청자 발표 --
#치킨 담청자: 1
#커피 담청자: [2, 3, 4]
# -- 축하합니다 --

from random import *
#lst = [1,2,3,4,5]
#print(lst)
#shuffle(lst)
#print(lst)
#print(sample(lst, 1))

user = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
#user = range(1, 21) # 1부터 20까지 숫자 생성
#user = list(user) # 변수를 리스트로 변경
shuffle(user)
chicken = sample(user, 1)
coffee = sample(user, 3)

print("-- 담청자 발표 --")
print("치킨 담청자: " + str(chicken))
print("커피 담청자: " + str(coffee))
print("-- 축하합니다 --")

# 정답
users = range(1, 21) # 1부터 20까지 숫자 생성
users = list(users) # 변수를 리스트로 변경
shuffle(users)

winners = sample(users, 4) # 4명 중 1명은 치킨, 3명은 커피
print("-- 담청자 발표 --")
print("치킨 담청자: {0}".format(winners[0]))
print("커피 담청자: {0}".format(winners[1:]))
print("-- 축하합니다 --")