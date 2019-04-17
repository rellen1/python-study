# divmod(5,2)

# a = input('첫 번째 숫자를 입력하세요: ')
# b = input('두 번째 숫자를 입력하세요: ')
 
# print(a + b)

# c = int(input('첫 번째 숫자를 입력하세요: '))
# d = int(input('두 번째 숫자를 입력하세요: '))
 
# print(c + d)




# a,b,c,d = map(int, input().split())
# e = int((a+b+c+d) / 4)
# print(e)



# print(1,end='')
# print(2,end=' ')
# print(3)
# print(4)



# import sys
# print(sys.getrefcount(1000))    # 2: 처음 레퍼런스 카운트는 2
 
# x = 1000                        # x에 1000을 저장
# print(sys.getrefcount(1000))    # 3: 1000을 한 번 사용하여 레퍼런스 카운트 1 증가
 
# y = 1000                        # y에 1000을 저장
# print(sys.getrefcount(1000))    # 4: 1000을 한 번 사용하여 레퍼런스 카운트 1 증가
 
# print(x is y)    # True: x와 y가 같은 객체를 가리키고 있으므로 True가 나옴


a,b,c,d= map(int, input().split())
print(a>=90 and b > 80 and c>85 and d >=80)