#!/usr/bin/python3

from sys import stdin
import copy

# TODO Not accepted (Runtime exception)
for _ in range(3):
    N, K = map(int, stdin.readline().rstrip().split())
    R, S, P = map(int, stdin.readline().rstrip().split())
    T = stdin.readline().rstrip()

    # print('{} {} {} {} {} {}'.format(N, K, R, S, P, T))

    history = []

    HANDS = ["r", "s", "p"]
    WIN_HANDS = {"r": "p", "p": "s", "s": "r"}
    WIN_SCORE = {"r": R, "s": S, "p": P}

    total_score = 0
    for i, cpu_hand in enumerate(T):
        unavailable_hand = history[-K] if i >= K else ""
        hand = WIN_HANDS[cpu_hand]

        if hand != unavailable_hand:
            history.append(hand)
            total_score += WIN_SCORE[hand]
        else:
            if i + K < len(T) and WIN_HANDS[T[i + K]] != hand:
                history.append(WIN_HANDS[T[i + K]])
                total_score += WIN_SCORE[WIN_HANDS[T[i + K]]]
            else:
                tmp_hands = copy.deepcopy(HANDS)
                tmp_hands.remove(hand)
                history.append(tmp_hands[0])
    # print(history)
    print(total_score)
