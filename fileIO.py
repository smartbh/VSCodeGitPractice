# score_file = open("score.txt", "w", encoding="utf8") #utf8 안해주면 한글깨짐
# print("수학 : 0", file = score_file)
# print("영어 : 50", file = score_file)
# score_file.close()

# score_file = open("score.txt", "a", encoding="utf8")
# #a는 뒤에 이어서 쓰기 (append), w는 처음부터 덮어 쓰기

# score_file.write("과학 : 80")
# score_file.write("\n코딩 : 100")
# #print로 할땐 자동 줄바꿈이 됨, write쓸때는 줄바꿈 명시적으로 해줘야
# score_file.close()


# #파일 읽어보기
# score_file = open("score.txt", "r", encoding="utf8")

# # print(score_file.read())
# print(score_file.readline()) #줄별로 읽기, 한 줄 읽고 커서는 다음줄로
# #줄바꿈 싫으면 end = ""해도 됨
# print(score_file.readline(),end = "")
# print(score_file.readline(),end = "")
# print(score_file.readline(),end = "")
# score_file.close()

#몇줄인지 모를 파일 열때는 반복문으로 해줘야

# score_file = open("score.txt","r",encoding="utf8")
# while True:
#     line = score_file.readline()
#     if not line:
#         break
#     #print(line)
#     print(line, end="")

# score_file.close()

score_file = open("score.txt","r",encoding="utf8")
lines = score_file.readlines() #list 형태로 저장
for line in lines:
    print(line, end = "")
score_file.close()