#비밀번호 만들어보기
#사이트 별로 비밀번호 만들기
#규칙1 : http:// 부분 제외
# 처음 만나는 점 이후 부분은 제외 naver.com -> naver
# 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내'e' 갯수 + "!"로 비밀번호 작성
#예) nav51!

#url = "http://naver.com"
url = "http://google.com"

my_pss = url.replace("http://", "") #규칙1

print(my_pss)

dotIndex = my_pss.find(".")
my_pss = my_pss[:my_pss.index(".")]

password = my_pss[:3] + str(len(my_pss)) + str(my_pss.count("e")) + "!"

print(password)

print("{0} 의 비밀번호는 {1} 입니다.".format(url,password))