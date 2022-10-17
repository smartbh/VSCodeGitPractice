from tkinter import commondialog


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