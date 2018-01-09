#!/bin/python3
import math


def minimumLoss(prices):
    min_loss = math.inf

    sorted_prices = sorted(prices, reverse=True)

    for i in range(len(sorted_prices)-1):
        price = sorted_prices[i] - sorted_prices[i+1]
        if 0 < price < min_loss and prices.index(sorted_prices[i]) < prices.index(sorted_prices[i+1]):
            min_loss = price

    return min_loss

if __name__ == "__main__":
    n = int(input().strip())
    prices = list(map(int, input().strip().split(' ')))
    result = minimumLoss(prices)
    print(result)
