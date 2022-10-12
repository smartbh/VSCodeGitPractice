# #퀴즈,  
# 50명의 손님중
# 승객별 운행 소요 시간은 5~50분 사이의 난수로 정해짐
# 소요시간 5~15분 사이의 손님만 매칭해야함

from random import *

count = 0
for i in range(1,51):
    time = randrange(5,51)
    if 5 <= time <= 15 :
        count+=1
        print("[0] {0}번째 손님 (소요시간 : {1})".format(i,time))
    else:
        print("[ ] {0}번째 손님 (소요시간 : {1})".format(i,time))

print("총 탑승 승객 : {0} 분".format(count))
