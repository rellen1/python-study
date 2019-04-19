# for i in range(100):
#     if i % 2 == 0:
#         continue
#     print(i)

# i = 0
# while i < 100:
#     i += 1
#     if i% 2 == 0:
#         continue
#     print(i)


# continue는 아래 코드를 건너뛰고 loop 문으로 다시 넘어가게됨
# pass 는 상관없이 바로 다음줄 실행.. 쓸모없을 것같지만 에러관리를 위해쓰는경우가 있음.. 에러가 발생하더라도 계속 코드 진행을 위해 쓰는 경우가있다
# break는 아예 Loop문을 나감


# count = int(input('반복횟수지정 : '))
# i = 0
# while True:
#     print(i)
#     i += 1
#     if i == count:
#         break


# count = int(input('반복 지정 : '))
# for i in range(count + 1):
#     if i % 2 == 1:
#         continue
#     print(i)


start, stop = map(int, input().split())
i = start
while True:
    if i % 10 == 3:
        i += 1
        continue
    if i > stop:
        break
    print (i, end=' ')
    i += 1
