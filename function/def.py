def open_account():
    print("새로운 계좌가 생성되었습니다.")

open_account()

def deposit(balance, money):
    print("입금이 완료되었습니다. 잔액은 {0}원입니다.".format(balance + money))
    return balance + money

def withdraw(balance, money):
    if balance >= money:
        print("출금이 완료되었습니다. 잔액은 {0}원입니다.".format(balance - money))
        return balance - money
    else:
        print("출금이 완료되지 않았습니다. 잔액은 {0}원입니다.".format(balance))
        return balance

def withdraw_night(balance, money):
    commission = 100 # 수수료 100원
    if balance >= money:
        print("출금이 완료되었습니다. 잔액은 {0}원입니다.".format(balance - money - commission))
        return commission, balance - money - commission
    else:
        print("출금이 완료되지 않았습니다. 잔액은 {0}원입니다.".format(balance))
        return balance
    
#입금
balance = 0
balance = deposit(balance, 1000)

#출금
balance = withdraw(balance, 500)

#저녁 출금
commission, balance = withdraw_night(balance, 300)
print("수수료는 {0}원이며, 잔액은 {1}원입니다.".format(commission, balance))