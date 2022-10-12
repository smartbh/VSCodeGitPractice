#while
# customer = "토르"
# index = 5

# while index >= 1:
#     print("{0}, 커피가 준비됐습니다, {1}".format(customer,index))
#     index-= 1
#     if index == 0:
#         print("커피는 폐기처분됐습니다.")

customer = "토르"
person = "unknown"

while person != customer:
    print("{0}, 커피가 준비됐습니다.".format(customer))
    person = input("이름이 어떻게 되세요? ")


absent = [2,5] #결석

no_book = [7]

for student in range(1,11):
    if student in absent:
        continue
    elif student in no_book:
        print("오늘 수업은 여기까지 {0}는 교무실로 따라와".format(student))
        break
    print("{0}, 책을 읽어봐".format(student))