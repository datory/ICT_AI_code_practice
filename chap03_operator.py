'''
문제 1] 사용자에게 10000원 이하의 금액을 입력 받아 동전으로 교환해주는 코드를 작성하세요.
        단, 동전을 큰 동전 순으로 교환합니다.
        
[프로그램 실행 예]

만원 이하의 금액을 입력하세요: 7777

500원 짜리 동전 15개
100원 짜리 동전 2개
50원 짜리 동전 1개
10원 짜리 동전 2개
나머지 금액 7원
'''

# my code
refund = int(input())
refund_a_1 = refund%500
refund_a_2 = refund//500
refund_b_1 = refund_a_1%100
refund_b_2 = refund_a_1//100
refund_c_1 = refund_b_1%50
refund_c_2 = refund_b_1//50
refund_d_1 = refund_c_1%10
refund_d_2 = refund_c_1//10
refund_e_2 = refund_d_1//1
print(refund_a_2)
print(refund_b_2)
print(refund_c_2)
print(refund_d_2)
print(refund_e_2)

# teacher's code
money = int(input('만원 이하의 금액을 입력하세요:'))

print('\n500원 짜리 동전 ' + str(money // 500) + '개')

money = money % 500
print('100원 짜리 동전 ' + str(money // 100) + '개')

money = money % 100
print('50원 짜리 동전 ' + str(money // 50) + '개')

money = money % 50
print('10원 짜리 동전 ' + str(money // 10) + '개')

print('나머지 금액 ' + str(money % 10) + '원')



'''
문제 2] 사용자에게 하나의 실수를 입력으로 받아 버림과 반올림 결과를 출력하는 코드를 작성하세요.

[실행 예 1]                                   [실행 예 2]

하나의 실수를 입력하세요: 3.6                 하나의 실수를 입력하세요: 3.4

버림: 3                                       버림: 3
반올림: 4                                     반올림: 3
'''

# teacher's code
num = float(input('하나의 실수를 입력하세요: '))

print('버림:', int(num))
print('반올림:', int(num+0.5))