#!/usr/bin/python3

# 리스트 []
#지하철 칸 별로 10명, 20명, 30명

# 각 변수에 따로 값을 넣어줌
subway1 = 10
subway2 = 20
subway3 = 30

# 리스트를 이용하여 순서대로 입력
subway = [10, 20, 30]
subway_human = ["유재석", "조세호", "박명수"]

# 조세호씨가 몇 번째 칸에 타고 있는가?
print(subway_human.index("조세호"))

# 하하가 다음 정류장에 다음 칸에 탐
subway_human.append("하하")
print(subway_human)

# 정형돈을 유재석, 조세호 사이에 태움
subway_human.insert(1, "정형돈")
# 변수.insert(index, "value")
print(subway_human)

# 지하철에 있는 사람을 한 명씩 뒤에서 꺼냄
print(subway_human.pop())
print(subway_human)

# 같은 이름의 사람이 몇명이 있는지 확인
subway_human.append("유재석")
print(subway_human)
print(subway_human.count("유재석")) # 동일 값이 몇 번 나오는지?

# 순서대로 정렬
num_list = [4,2,3,5,1]
num_list.sort()
print(num_list)

# 역순서대로 정렬
num_list.reverse()
print(num_list)

# 리스트 모두 지우기
num_list.clear()
print(num_list)

# 다양한 자료형 함께 사용
mix_list = ["조세호", 20, True]
print(mix_list)

# 리스트 합치기
n_list = [4,2,3,5,1]
mix_list.extend(n_list)
print(mix_list)