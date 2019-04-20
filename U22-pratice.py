# a = [ 10, 20, 30 ]
# print(a)
# len(a)
# a.append(500)
# print(a)
# len(a)


# >>> a = [i for i in range(10)]        # 0부터 9까지 숫자를 생성하여 리스트 생성
# >>> a
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# >>> b = list(i for i in range(10))    # 0부터 9까지 숫자를 생성하여 리스트 생성
# >>> b
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

#구구단
# a = [ i*j for i in [2] for j in range(1,10)]

# # 리스트 정수로 변경
# a = [1.2, 2.5, 3.7, 4.6]
# a = list(map(int, a))

# 내가 푼거~~~~~~~~~~~~~~~~~
# a = []
# b = list(map(int, input().split()))
# c = b[0]

# while c <= b[1]:
#     a.append(pow(2,c))
#     c += 1

# a.pop(1)
# a.pop(-2)

# print(a)


# 해답지~~~~~~~~~~~~~~
start, stop = map(int, input().split())
a = [2 ** i for i in range(start,stop+1)]
a.pop(1)
a.pop(-2)
print(a)