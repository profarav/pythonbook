x = 'CALIFORNIA$'
for i in range(len(x)):
    y = x[-i:] + x[:-i]
    print(y)
