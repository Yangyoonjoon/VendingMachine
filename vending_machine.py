menu = ['콜라', '사이다', '코코아', '커피']
price = [190, 270, 350, 410]
amount = [10, 10, 10, 10]
money = 0

def showmenu():
    print('자판기 메뉴')
    n = len(menu)
    for i in range(n):
        print(str(i+1)+'.', menu[i], '\t', str(price[i])+'원')

    print()

def inputmoney():
    while True:
        try:
            m = int(input('돈 투입:'))
        except:
            print('입력 오류\n')
        else:
            break
    return m

def selectmenu():
    print()
    while True:
        try:
            sel = int(input('음료를 고르세요(종료:0):'))
        except:
            print('입력 오류')
            return 0
        else:
            break

    if sel == 0:
        return -1

    # 메뉴 번호 체크
    if sel >= 1 and sel <= len(menu):
        # 수량 체크
        if amount[sel-1] > 0:
            amount[sel-1] -= 1
            # 금액 체크
            if money >= price[sel-1]:
                print(menu[sel-1], '구입완료')
                return price[sel-1]
            else:
                print('잔액 부족')
                return 0
        else:
            print('수량 부족')
            return 0
    else:
        print('없는 메뉴입니다')
        return 0

showmenu()
money = inputmoney()
print('투입 금액은', money)

while True:
    result = selectmenu()
    if result == -1:
        break

    money -= result
    print('잔액:', money)

# 잔돈
x500 = money//500
result = money%500

x100 = result//100
result = money%100

x50 = result//50
result = money%50

x10 = result//10
result = money%10

print('\n잔돈')
print('500원:', str(x500) + '개')
print('100원:', str(x100) + '개')
print('50원:', str(x50) + '개')
print('10원:', str(x10) + '개')

print('\n자판기 종료')