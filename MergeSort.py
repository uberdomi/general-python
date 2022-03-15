

x = []
for i in range(1,31):
    x.append(i) if i%3 != 0 else x.append(int(i/3))

# while (i := input('Add to list; to stop type in \'stop\': ')).lower() != 'stop':
  #  if type(i) == int
  #   x.append(i)


print(x)


def merge_sort(x,leq):
    le = len(x)
    if le != 1:
        x1 = x[:int(le/2)]
        x2 = x[int(le/2):]
        x1 = merge_sort(x1,leq)
        x2 = merge_sort(x2,leq)
        i1, i2 = 0,0
        x = []
        for i in range(0,le):
            if i1 == len(x1):
                while i2 < len(x2):
                    x.append(x2[i2])
                    i2 += 1
            elif i2 == len(x2):
                while i1 < len(x1):
                    x.append(x1[i1])
                    i1 += 1
            elif leq(x1[i1],x2[i2]):
                x.append(x1[i1])
                i1 += 1
            else:
                x.append(x2[i2])
                i2 += 1
    return x


leq = lambda i,j: int(i)<=int(j) if int(i)%3 == int(j)%3 else int(i+1)%3>=int(j+1)%3

# for i in x:
  #   print(i, " not greater than 5?: ", leq(i,5))


if not int(leng := len(x)) == 1:
    x1 = x[:int(leng / 2)]
    x2 = x[int(leng / 2):]
    print(x1)
    print(x2)


print(merge_sort(x,leq))
#x = merge_sort(x, lambda i,j: i<=j)
#print(x)