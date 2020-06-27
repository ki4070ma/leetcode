#!/usr/bin/python3

for _ in range(3):
    N, M, K = map(int, input().rstrip().split())
    As = [int(x) for x in input().rstrip().split()]
    Bs = [int(x) for x in input().rstrip().split()]
    ln_max = len(As)
    lm_max = len(Bs)
    ln = 0
    lm = 0
    count_time = 0
    count_book = 0
    while True:
        if count_time >= K:
            break
        if ln >= ln_max and lm >= lm_max:
            break
        if ln >= ln_max and lm < lm_max:
            count_time += Bs[lm]
            lm += 1
        elif lm >= lm_max and ln < ln_max:
            count_time += As[ln]
            ln += 1
        elif As[ln] > Bs[lm]:
            if count_time + Bs[lm] >= K:
                break
            count_time += Bs[lm]
            lm += 1
        else:
            if count_time + As[ln] >= K:
                break
            count_time += As[ln]
            ln += 1
        # print(f'ln: {ln}')
        # print(f'lm: {lm}')
        count_book += 1
        # print(count_time)
    # print('----')
    # print(N-1, M-1)
    print(count_book)
