#튜플 연습
#리스트보다 빠르지만 값 변경이 안됨
#데이터가 변경 안될 애들만 해주는게 좋음

menu = ("돈까스", "치즈까스") #이 이후에 추가나 변경이 안됨

print(menu[0])
print(menu[1])

#튜플은 한번에 다른 변수에 다른 값들을 넣어줄수도 있음
(name, age, hobby) = ("김종국", 20, "코딩")
print(name, age, hobby)