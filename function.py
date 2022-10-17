from tkinter import commondialog

from pip import main


def open_account():
    print("새로운 계좌가 생성되었습니다.")

def deposit(balance, money):
    print("입금이 완료되었습니다. 잔액은 {0}원 입니다.".format(balance + money))
    return balance + money


def withdraw(balance, money):
    if(balance >= money):
        print("출금이 완료되었습니다. 잔액은 {0}원 입니다.".format(balance - money))
        return balance - money
    else:
        print("잔액이 부족합니다.")
        return balance

def withdraw_night(balance, money):#저녁에 출금
    commission = 100
    return commission, balance - money - commission
    


balance = 0
balance = deposit(balance, 2000)
#balance = withdraw(balance, 1000)
#balance = withdraw(balance, 3000)

commission, balance = withdraw_night(balance, 500)

print("수수료는 {0}원이며 잔액은 {1}원 입니다.".format(commission,balance))

print(balance)



#함수에 default값 주기

def profile(name, age = 17, main_lang = "한국어"):
    print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}"  
    .format(name, age, main_lang))

profile("김태호",16,"파이썬")
profile("유재석")

#키워드

def profile(name, age, main_lang):
    print(name, age, main_lang)

#함수에서 전달받는 매개변수들을 키워드 =로 넣어주면
#매개변수 순서가 바뀌어도 매개변수를 잘 입력할수있다.
profile(name = "유재석", main_lang="파이썬",age=20)



#가변인자
# def profile(name, age, main_lang, lang1,lang2,lang3):
#     print("이름 : {0}\t나이:{1}\t".format(name,age), end=" ")
#     print(main_lang,lang1,lang2,lang3)

#서로 다른 개수의 값을 넣어줄때는 *로 시작되는 가변인자 매개변수도 가능
def profile(name, age, *language):
    print("이름 : {0}\t나이:{1}\t".format(name,age), end=" ")
    for lang in language:
        print(lang, end = " ")
    print()

profile("유재석",20,"python","java","c++","c")
profile("김태호",20,"코틀린","스위프트")

