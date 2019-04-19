# for i in range(1,101):
#     print(i)

# for i in range(1,101):
#     if i % 3 == 0 and i % 5 ==0:
#         print('FizzBuzz')    
#     elif i % 3 == 0:
#         print('Fizz')
#     elif i % 5 == 0:
#         print('Buzz')
#     else:
#         print(i)

# for i in range(1,101):
#     print('Fizz' * (i % 3 == 0) + 'Buzz' * (i % 5 == 0) or i)

a = list(map(int, input().split()))
for i in range(a[0],a[1]):
    if i % 35 == 0:
        print('FizzBuzz')
    elif i % 5 == 0:
        print('Fizz')
    elif i % 7 == 0:
        print('Buzz')
    else:
        print(i)