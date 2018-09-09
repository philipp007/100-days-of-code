#!/bin/python3
def string_add(a, b):
    padding = max(len(a), len(b))
    a = a.zfill(padding)
    b = b.zfill(padding)
    remainder = 0
    result = ''

    for i in range(padding-1, -1, -1):
        sum = int(a[i]) + int(b[i]) + remainder
        remainder = 1 if sum > 9 else 0
        result += str(sum % 10)

    return ''.join(reversed(result))


def power_of_eleven(power):
    if power <= 1:
        return "11"

    previous_power = power_of_eleven(power-1)
    previous_power_times_ten = previous_power + "0"
    return string_add(previous_power, previous_power_times_ten)


def count_ones(str):
    return str.count('1')


if __name__ == '__main__':
    N = int(input())
    power = power_of_eleven(N)
    print(count_ones(power))
