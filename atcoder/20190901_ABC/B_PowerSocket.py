#!/usr/bin/python3

num_power_taps, target_tap_num = map(int, input().split())

if target_tap_num == 1:
    print(0)
else:
    print(-(-(target_tap_num - 1) // (num_power_taps - 1)))
