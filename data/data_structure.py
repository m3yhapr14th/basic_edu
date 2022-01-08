#!/usr/bin/python3
# 자료구조의 변경

# 세트
menu = {"커피", "우유", "주스"}
print(menu, type(menu))

# 리스트로 변경
menu = list(menu)
print(menu, type(menu))

# 튜플로 변경
menu = tuple(menu)
print(menu, type(menu))