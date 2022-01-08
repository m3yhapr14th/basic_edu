# 당신의 회사에서는 매주 1회 작성해야 하는 보고서가 있습니다.
# 보고서는 항상 아래와 같은 형태로 출력되어야 합니다.

# - X 주차 주간보고 -
# 부서 : 
# 이름 : 
# 업무 요약 : 

# 1주차부터 50주차까지의 보고서 파일을 만드는 프로그램을 작성하시오.
# 조건: 파일명은 '1주차.txt', '2주차.txt', ...와 같이 만듭니다.

# 내가 한거
for i in range(1, 3):
    report = open("{0}주차.txt".format(i), "w", encoding="utf-8")
    print("부서: 보안팀", file=report)
    print("이름: xxx", file=report)
    print("업무 요약: abcdefg", file=report)
    report.close()

# 정답
for i in range(1, 4):
    #with open("{0}주차.txt".format(i), "w", encoding="utf-8") as report:
    with open(str(i) + "주차.txt", "w", encoding="utf-8") as report:
        report.write("- {0}주차 주간 보고\n".format(i))
        report.write("부서: 보안팀\n")
        report.write("이름: xxx\n")
        report.write("업무 요약: abcdefg")
