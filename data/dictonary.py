#!/usr/bin/python3
# 사전 {key:value}
# 변경되는 값

cabinet = {3:"유재석", 100:"김태호"}
# 방법1
print(cabinet[3])
print(cabinet[100])

# 방법2
print(cabinet.get(3))
#print(cabinet[5]) # 주의사항//사전에 값이 없을 경우 []로 출력할 경우 프로그램 종료
#print("Hello")

print(cabinet.get(5)) # 값이 없을때 get을 이용하면 시도함
print("Hello")

print(cabinet.get(5, "사용 가능"))

print(3 in cabinet)

# 새로운 값
cabinet["C-10"] = "조세호"
print(cabinet)

# 값 업데이트
cabinet[3] = "김종국"
print(cabinet)

# 값 삭제
del cabinet[3]
print(cabinet)

# Only keys
print(cabinet.keys())

# Only value
print(cabinet.values())

# both key and value
print(cabinet.items())

# all delete
cabinet.clear()
print(cabinet)
