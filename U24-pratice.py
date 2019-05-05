# import string

# a = input().split()
# c = 0

# for i in range(len(a)):
#     a[i] = a[i].strip(string.punctuation).strip()
#     if a[i] == 'the':
#             c+=1


# print(c) 


###################################

a = list(map(int,input().split(';')))
a.sort(reverse=True)

for i in range(len(a)):
        print('{0:>9,}'.format(a[i]))



