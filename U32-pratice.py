files = input().split()

# print(list(lambda a : a.zfill(7) if len(a) == 5 else a.zfill(8),files))

print(list(map(lambda a : '{0:0>7}'.format(a) if a[-4] == '.' else '{0:0>8}'.format(a), files)))