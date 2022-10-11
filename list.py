#리스트 []
# 지하철 칸별로 10명, 20명 30명

#subway1 = 10
#subway2 = 20
#subway3 = 30

subway = [10,20,30]
print(subway)

subway = ["유재석", "조세호", "박명수"]
print(subway)

print(subway.index("조세호"))

#하하가 다음 정류장에서 다음칸에 탐
subway.append("하하")
print(subway)

#정형돈을 유재석과 조세호 사이에 넣기, append는 늘 마지막에
subway.insert(1,"정형돈")
print(subway)

#지하철에 있는 사람을 한면ㅇ씩 뒤에서 꺼냄
print( subway.pop())
print(subway)

#print( subway.pop())
#print(subway)

#print( subway.pop())
#print(subway)

# 같은 이름의 사람이 몇이나 있는지 확인
subway.append("유재석")
print(subway)
print(subway.count("유재석"))

#정렬도 가능
num_list = [5,2,4,1,2,3,7,9]
num_list.sort() #정방향 정렬, 오름차순
print(num_list)

num_list.reverse() #역방향 정렬, 내림차순
print(num_list)

num_list.clear()
print(num_list)

#다양한 자료형 함께 사용
mix_list = ["조세호", 1, True]
num_list = [5,2,4,1,2,3,7,9]
print(mix_list)

mix_list.extend(num_list)
print(mix_list)