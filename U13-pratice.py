# x = 10
# if x != 10:
#     print('x의 숫자는')
# print('a')


# a = int(input())
# b = input()

# if b == 'Cash3000':
#     print (a - 3000)

# if b == 'Cash5000':
#     print (a - 5000)



# if False:
#     print('참')
# else:
#     print('거짓')    # False는 거짓


# if '':    # 빈 문자열
#     print('참')
# else:
#     print('거짓')    # 빈 문자열은 거짓


# if 0:
#     print('참')
# else:
#     print('거짓')    # 0은 거짓


# if None:
#     print('참')
# else:
#     print('거짓')    # None은 거짓






a = input().split()
a = list(map(int,a))

if 0 <= a[0] <= 100 and 0 <= a[1] <= 100 and 0 <= a[2] <= 100 and 0 <= a[3] <= 100:
    result = (a[0]+a[1]+a[2]+a[3]) / 4

    if result >= 80:
        print('합격')
    else:
        print('불합격')

else:
    print('잘못된 점수')




