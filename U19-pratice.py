# for i in range(5):
#     for j in range(4):
#         print('j:', j, sep='', end=' ')
#     print('i:', i, '\n', sep='')
    
# for i in range(5):
#     for j in range(5):
#         if i <= j:
#             print('*',end='')
#     print()

# for i in range(5):
#     for j in range(5):
#         if j == i:
#             print('*',end='')
#         else:
#             print(' ',end='')
#     print()


# for i in range(5):
#     for j in range(5):
#         if j < i:
#             print(' ',end='')
#         else:
#             print('*', end='')
#     print()




#     *
#    ***
#   *****
#  *******
# *********

a = int(input())
b = a
bb = a-1
for i in range(a):
    for j in range(b):
        if j < bb:
            print(' ', end='')
        else:
            print('*', end='') 
    print()
    b += 1



for i in range(height):
    for j in reversed(range(height)):
        if j > i:
            print(' ', end='')
        else:
            print('*', end='')
                for j in range(height):
        if j < i:
            print('*', end='')
    print()