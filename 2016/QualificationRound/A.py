def doit(i,n,s):
    new_n = i*n
    if new_n == 0:
        return 'INSOMNIA'
    s = s.union(set(list(str(new_n))))
    if len(s) == 10:
        return new_n
    else:
        return doit(i+1,n,s)

t = int(input())
for i in range(1, t+1):
    n = int(input())
    res = doit(1,n,set())
    print('Case #{}: {}'.format(i, res))

