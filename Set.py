#세트(집합)
#중복안되고, 순서 없음

my_set = {1,2,3,3,3}

print(my_set)
#1,2,3만 출력, 중복은 출력 안함

java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"])

#교집합 출력해보기 (자바 파이선 모두 있는 사람)
print(java & python)
print(java.intersection(python))

#합집합 출력해보기
print(java | python)
print(java.union(python))

#차집합
print(java - python)
print(java.difference(python))

# python 할 줄 아는 사람이 늘어남
python.add("김태호")
print(python)

# java를 까먹는다
java.remove("김태호")
print(java)