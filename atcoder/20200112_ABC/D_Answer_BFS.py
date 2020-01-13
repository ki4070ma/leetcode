#!/usr/bin/python3

# https://atcoder.jp/contests/abc151/submissions/9492761

from collections import deque

# BFS
for _ in range(2):
    h, w = map(int, input().split())
    a = [input() for _ in range(h)]
    r = 0
    for i in range(h):
        for j in range(w):
            if a[i][j] == '.':  # ブロックのマスはStart pointにはならず.
                b = list(map(list, a))  # 距離を格納するマトリクスの初期化
                q = deque()  # ★ポイント. 詳しくはAtCoderの解説動画. https://www.youtube.com/watch?v=1oLDDdWRu6Y
                b[i][j] = 0  # Start pointは全通り確認
                q.append((i, j))
                while(q):
                    i, j = q.popleft()
                    r = max(r, b[i][j])
                    d = 0
                    for i1 in range(i-1, i+2):  # h: i-1, i, i+1
                        if 0 <= i1 < h:  # i1がリストから外れていないかどうか
                            # w: jの上下はrange(j, j+2, 2)なのでjのみ
                            # w: jの左右はrange(j-1,j+2, 2)なのでj-1, j+1で左右
                            for j1 in range(j-d, j+2, 2):
                                if 0 <= j1 < w and b[i1][j1] == '.':
                                    b[i1][j1] = b[i][j] + 1  # 距離を格納
                                    q.append((i1, j1))
                        d ^= 1  # d = d ^ 1に同じ. 0, 1 => 1, 0 / 2, 3 => 3, 2
                                # a ^ b: XOR: 排他的論理和.
                                # これは, 0 -> 1 -> 0とするため. あるマス目に対して, 1行目は上だけ,
                                # 2行目は左と右の2つ, 3行目は下だけ
    print(r)
