#print("대기번호 : 1")


for waiting_no in range(1,6):
    print("대기번호 : {0}".format(waiting_no))

starbucks = ["아이언맨","토르","헐크"]

for customer in starbucks:
    print("{0}님, 커피가 준비됐습니다.".format(customer))

#한줄로 for문 쓰기

#출석 번호 앞에 100씩 붙여보기
students = [1,2,3,4,5]
print(students)
students = [i+100 for i in students]
print(students)

#이름을 문자열 길이로 변환
students = ["Iron man", "Thor", "Hulk"]
print(students)
students = [len(i) for i in students]
print(students)

#이름 모두 대문자로 바꾸기
students = ["Iron man", "Thor", "Hulk"]
print(students)
students = [i.upper() for i in students]
print(students)
