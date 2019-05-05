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



# a = [[0 for j in range(2)] for i in range(3)]



# a = [[0] * i for i in [3, 1, 3, 2, 5]]


# a = [3, 1, 3, 2, 5]    # 가로 크기를 저장한 리스트
# b = []    # 빈 리스트 생성
# for i in a:      # 가로 크기를 저장한 리스트로 반복
#     line = []    # 안쪽 리스트로 사용할 빈 리스트 생성
#     for j in range(i):    # 리스트 a에 저장된 가로 크기만큼 반복
#         line.append(0)
#     b.append(line)        # 리스트 b에 안쪽 리스트를 추가
# print(b)

col,row = list(map(int, input().split()))

matrix = []
for i in range(row):
    matrix.append(list(input()))

for i in range(row):                # 첫번째 배열 검사(처음 이중 for문)으로 *인지 . 인지 확인하고
    for j in range(col):

        if matrix[i][j] == '*':
            continue

        if matrix[i][j] == '.':     # .이면 숫자를 0으로 초기화한다.
            matrix[i][j] = 0

            for ii in range( i-1, i+2 ):    # 두번째 배열 검사로 .일 경우 해당 배열의 -1에서 +1수준까지의 배열을 검사한다.
                for jj in range( j-1, j+2 ):
                    if ii < 0 or ii == row:     # 다만 해당 배열이 음수이거나 처음에 받은 입력값 이상이면 아무행동도 하지않는다.
                        continue
                    if jj < 0 or jj == col:
                        continue
                    if matrix[ii][jj] == '*':   # 두번째 배열 검사에서 *일 경우 첫번째 배열 값에 +1을 한다. 
                        matrix[i][j] += 1                    

for i in matrix:
    for j in i:
        print(j, end='')
    print()