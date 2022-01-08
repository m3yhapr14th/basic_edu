# 가변 인자
# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     print("이름: {0}\t나이: {1}\t".format(name, age), end=" ") # end 변수에 " " 같이 해놓으면 같은 줄에 생성
#     print(lang1, lang2, lang3, lang4, lang5)

# profile("유재석", 20, "Python", "Java", "C", "C++", "C#")
# profile("김태호", 25, "Kotlin", "Swift", "", "", "")

# 유재석이 할 수 있는 lang이 추가됨
def profile(name, age, *language):
    print("이름: {0}\t나이: {1}\t".format(name, age), end=" ") # end 변수에 " " 같이 해놓으면 같은 줄에 생성
    for lang in language:
        print(lang, end=" ")
    print()

# 서로 다른 lang 값(수)를 넣어줄 경우 위와 같이 정의함
profile("유재석", 20, "Python", "Java", "C", "C++", "C#")
profile("김태호", 25, "Kotlin", "Swift")
