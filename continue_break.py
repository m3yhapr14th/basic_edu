#!/usr/bin/python3

absent = [2, 5] # 결석
no_book = [7]
for student in range(1, 11):
    if student in absent:
        continue # 조건에 있을 경우 넘어가고 계속해서 반복문 실행

    elif student in no_book:
        print("오늘 수업 여기까지. {0}번은 교무실로 따라와".format(student))
        break # 조건에 충족할 경우 반복문 탈출
    print("{0}번, 책 읽어".format(student))
