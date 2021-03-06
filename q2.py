# _*_ coding: utf-8 _*_

"""题目：企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；20万到40万之间时，高于20万元的部分，可提成5%；40万到60万之间时高于40万元的部分，可提成3%；60万到100万之间时，高于60万元的部分，可提成1.5%，高于100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？"""

def direct():
    interest = int(input('净利润：'))
    if 0 < interest <= 100000:
        boun = interest * 0.1
    elif 100000 < interest <= 200000:
        boun = 100000 * 0.1 + (interest - 100000) * 0.075
    elif 200000 < interest <= 400000:
        boun = 100000 * 0.1 + 100000 * 0.075 + (interest - 200000) * 0.05
    elif 400000 < interest <= 600000:
        boun = 100000 * 0.1 + 100000 * 0.075 + 200000 * 0.05 + (interest - 400000) * 0.03
    elif 600000 < interest <= 1000000:
        boun = 100000 * 0.1 + 100000 * 0.075 + 200000 * 0.05 + 200000 * 0.03 + (interest - 600000) * 0.015
    elif 1000000 < interest:
        boun = 100000 * 0.1 + 100000 * 0.075 + 200000 * 0.05 + 200000 * 0.03 + 400000 * 0.015 + (interest - 1000000) * 0.01
    print(boun)


def brief():
    interest = int(input("净利润："))
    a = [1000000, 600000, 400000, 200000, 100000, 0]
    b = [0.01, 0.015, 0.03, 0.05, 0.075, 0.1]
    c = 0
    for n in range(len(a)):
        if interest > a[n]:
            c += (interest- a[n]) * b[n]
            interest = a[n]
    print(c)



brief()
