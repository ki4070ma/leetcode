#!/usr/bin/python3

for _ in range(10):
    print('***START')
    N, A, B = map(int, input().rstrip().split())
    if A == 0:
        ret = 0
    elif A + B == 0:
        ret = 0
    else:
        tmp1 = int(N / (A + B)) * A
        tmp2 = 0
        if A > N % (A + B):
            tmp2 = N % (A + B)
        else:
            tmp2 = A
        ret = tmp1 + tmp2
    print(ret)
    assert int(input().rstrip()) == ret

# print(N, A, B)
# print('b' * A + 'r' * B)
# mod = N % (A + B)
# print('***start')
# print(('b' * A + 'r' * B)[:(N % (A + B))].count('b'))
# print('***end')
# # print(('b'*A+'r'*B)[:)])
#
