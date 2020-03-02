#!/usr/bin/python3

for _ in range(8):
    N, M = map(int, input().rstrip().split())
    RET = -1
    if N == 0:
        RET = -1
    else:
        d = {}
        for _ in range(M):
            s, c = map(int, input().rstrip().split())
            if s == 0 or s > N or (s in d.keys() and c != d[s]):
                success_flg = False
                RET = -1
                break
            else:
                d[s] = c
        else:
            str_ans = '0' * N
            for s, c in d.items():
                if s == 1 and c == 0 and N != 1:
                    RET = -1
                    break
                str_ans = str_ans[:s-1] + str(c) + str_ans[s:]
            else:
                if str_ans[0] == '0' and N != 1:
                    str_ans = '1' + str_ans[1:]
                RET = int(str_ans)
    assert RET == int(input().rstrip())
    print(RET)
    print(input().rstrip())
