#!/usr/bin/python3
# 튜플 ()
# 불변값 **변하지 않는다

menu = ("돈까스", "치즈까스")
print(menu[0])
print(menu[1])

#menu.add("생선가스") # 에러

name = "김종국"
age = 20
hobby = "코딩"
print(name, age, hobby)

# 한꺼번에 튜플 등록
(name, age, hobby) = ("김종국", 20, "코딩")
print(name, age, hobby)