#!/usr/bin/python3
# 집합(세트) {}
# 중복 안됨, 순서 없음

my_set = {1,2,3,3,3}
print(my_set)

java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"])

# 교집합(java, python 모두 가능)
print(java & python)
print(java.intersection(python))

# 합집합 (java or python)
print(java|python)
print(java.union(python))

# 차집합 (java 가능, python 불가)
print(java - python)
print(java.difference(python))

# python 할 수 있는 사람 늘어남
python.add("김태호")
print(python)

# java 까먹음
java.remove("김태호")
print(java)