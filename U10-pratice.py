# a = input()
# a = int(a)
# b = tuple(range(-10,10,a))
# print(b)

# #리스트, 튜플, range, 문자열처럼 값이 연속적으로 이어진 자료형을 시퀀스 자료형(sequence types)
# a[len(a)-1]
# #시퀀스 자료형 중에서 튜플, range, 문자열은 읽기 전용임으로 임의의 인덱스를 변경 불가


# x = input().split()
# print(tuple(x[:-5]))



a = input()
b = input()
print(a[::2] + b[1::2])