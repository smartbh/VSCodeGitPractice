import pickle

#파일 형태로 저장하는것, 또 다른 파일입출력

# profile_file = open("profile.pickle", "wb")
# #b는 바이너리를 의미 피클에선 인코딩 해줄 필요 없음

# profile = {"이름":"박명수", "나이":30, "취미":["축구","골프","코딩"]}
# print(profile)
# pickle.dump(profile, profile_file) 
# #profile에 있는 정보를 file에 저장 -> dump
# profile_file.close()

profile_file = open("profile.pickle", "rb")
profile = pickle.load(profile_file)
#file에 있는 정보를 profile에 불러오기
print(profile)
profile_file.close()