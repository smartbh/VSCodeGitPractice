gun = 10 #전역변수

def checkpoint(soldiers):
    #gun = gun - soldiers #이대로 하면 지역변수 선언안되서
    #gun을 사용할수 없음
    #gun = 10 이렇게 지역변수로 선언해주거나
    global gun #이렇게 전역변수를 가져오거나 해야한다.
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))

def checkpoint(gun, soldiers):
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))
    return gun

print("전체 총 : {0}".format(gun))
gun = checkpoint(gun,2)
print("남은 총 : {0}".format(gun))