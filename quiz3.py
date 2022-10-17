#표준 체중을 구하는 프로그램을 작성하라

def std_weight(height,gender):
    if gender == "남":
        weight = height * height  * 22
        return weight
    else:
        weight = height * height  * 21
        return weight
height = 175
gender = "여"
print("키 {0}cm남자의 표준 체중은 {1}kg입니다.".format(height,round(std_weight(height/100,gender),2)))