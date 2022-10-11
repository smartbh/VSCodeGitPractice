#딕셔너리 연습
#리스트는 대괄호 [], 딕셔너리는 {} 중괄호
# key: value 순으로 묶임
cabinet = {3:"유재석", 100:"김태호"}

print(cabinet[3]) #대괄호 안에 키값
print(cabinet[100])

print(cabinet.get(3))
print(cabinet.get(5, "사용가능"))


print(3 in cabinet) #True
print(5 in cabinet) #False

#다양한 자료형으로 딕셔너리 가능

cabinet = {"A-3" : "유재석", "B-100":"김태호"}
print(cabinet["A-3"]) #대괄호 안에 키값
print(cabinet["B-100"])
print(cabinet)

#새로운 값 넣기
cabinet["A-3"] = "김종국"
cabinet["C-20 "] = "조세호"
print(cabinet)

#값 빼기도 가능
del cabinet["A-3"]
print(cabinet)

print(cabinet.keys()) #키값만 출력
print(cabinet.values()) #밸류값만 출력
print(cabinet.items()) #아이템만 출력

cabinet.clear() #모든 값 지우기
print(cabinet.keys()) #키값만 출력
print(cabinet.values()) #밸류값만 출력
print(cabinet.items()) #아이템만 출력