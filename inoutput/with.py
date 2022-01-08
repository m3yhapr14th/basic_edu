import pickle

with open("profile.pickle", "rb") as profile_file:
    print(pickle.load(profile_file))

# with문은 file.close 없이 알아서 종료됨

with open("study.text", "w", encoding="utf-8") as study_file:
    study_file.write("파이썬 열심히 공부")

with open("study.text", "r", encoding="utf-8") as study_files:
    print(study_files.read())