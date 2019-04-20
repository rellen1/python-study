# a = [[10, 20], [30, 40], [50, 60]]
 
# for i in range(len(a)):            # 세로 크기
#     for j in range(len(a[i])):     # 가로 크기
#         print(a[i][j], end=' ')
#     print()



# a = [[10, 20], [30, 40], [50, 60]]
 
# i = 0
# while i < len(a):    # 반복할 때 리스트의 크기 활용(세로 크기)
#     x, y = a[i]      # 요소 두 개를 한꺼번에 가져오기
#     print(x, y)
#     i += 1           # 인덱스를 1 증가시킴



# a = []    # 빈 리스트 생성
 
# for i in range(3):
#     line = []              # 안쪽 리스트로 사용할 빈 리스트 생성
#     for j in range(2):
#         line.append(0)     # 안쪽 리스트에 0 추가
#     a.append(line)         # 전체 리스트에 안쪽 리스트를 추가
 
# print(a)



a = [[0 for j in range(2)] for i in range(3)]



a = [[0] * i for i in [3, 1, 3, 2, 5]]


a = [3, 1, 3, 2, 5]    # 가로 크기를 저장한 리스트
b = []    # 빈 리스트 생성
for i in a:      # 가로 크기를 저장한 리스트로 반복
    line = []    # 안쪽 리스트로 사용할 빈 리스트 생성
    for j in range(i):    # 리스트 a에 저장된 가로 크기만큼 반복
        line.append(0)
    b.append(line)        # 리스트 b에 안쪽 리스트를 추가
print(b)