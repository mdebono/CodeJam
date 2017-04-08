def doit2(N, K, b):
    halfN = N//2
    if b > K:
        if N % 2 == 0:
            return (halfN, halfN-1)
        else:
            return (halfN, halfN)
    else:
        return doit2(halfN, K, b*2)

t = int(input())
for i in range(1, t+1):
    [N, K] = [int(x) for x in input().split(' ')]
    #print('{} {}'.format(N,K))
    (out1, out2) = doit2(N, K, 2)
    print('Case #{}: {} {}'.format(i, out1, out2))

