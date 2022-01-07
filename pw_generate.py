# 안내 문구 출력
print("Password is generated as an under format\n > [Default Word]@[Website Name]][Website Count]")

# URL 입력
url = input("URL: ")

# URL 축약
pw_info = url.replace("http://", "")
pw_info = pw_info.replace("https://", "")
pw_info = pw_info.replace("www.", "")
pw_info = pw_info[:pw_info.index(".")]

# 기본으로 들어갈 단어 입력
default = input("Default Word: ")

# 패스워드 생성
password = str(default) + "@" + str(pw_info[0].upper()) + str(pw_info[1:]) + str(len(pw_info))

# URL의 이름
name = pw_info[0].upper() + pw_info[1:]

print("{0}'s password is \"{1}\".".format(name, password))