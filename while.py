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