# a = input()

# b = True
# for i in range(len(a) // 2):
#     if a[i] != a[-1 -i]:
#         b = False
#         break

# print(b)



# a = input("단어 입력 : ")

# print(a == a[::-1])

# a = 'level'
# list(a)  ==  list(reversed(a))

# a = 'lever'
# a == ''.join(reversed(a))


# /////////////////////////////

# a = 'hello'

# for i in range(len(a) - 1):
#     print(a[i], a[i+1], sep='')

# ////////////////////////////////////

# a = 'thi is  python script'
# b = a.split()

# for i in range(len(b) -1 ):
#     print (b[i], b[i+1])

# a = int(input('숫자 입력 : '))
# b = input('문장 입력 :')
# c = b.split()

# if len(c) < a:
#     print('wrong bye')
# else:
#     c = zip(*[c[i::] for i in range(a)])
#     for i in n_gram:
#         print(i)

text = 'hello'
[text[i:] for i in range(3)]