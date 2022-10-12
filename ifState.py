weather = "맑음"
if weather == "비":
    print("우산을 챙기세요")
elif weather == "맑음":
    print("준비물 필요없음")
elif weather == "미세먼지":
    print("마스크써라")
else :
    print("집에있어")


temp = int(input("기온을 입력하세요 : "))
if 30 <= temp:
    print("존나덥다 벗고나가라")
elif 10 <= temp and temp < 30:
    print("놀기 좋은 날씨다")
elif 0 <= temp < 10:
    print("춥다 챙겨입어라")
else:
    print("얼어 뒤지니깐 나가지마라")
    