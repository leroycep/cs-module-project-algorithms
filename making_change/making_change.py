#!/usr/bin/python

import sys

class Change:
    def __init__(self, denominations, amounts=[], denom_len=None):
        if denom_len is None:
            denom_len = len(denominations)
        self.coins = [0] * denom_len
        for idx, _val in enumerate(self.coins):
            if idx >= len(amounts):
                break
            self.coins[idx] = amounts[idx]

    def __eq__(self, other):
        if len(self.coins) != len(other.coins):
            return False
        for coin, ocoin in zip(self.coins, other.coins):
            if coin != ocoin:
                return False
        return True

    def __hash__(self):
        sum = 0
        for idx, coin in enumerate(self.coins):
            sum += 10000000 ** idx * coin
        return sum

    def __repr__(self):
        return f"{self.coins}"

    def increment(self, denom_idx):
        new_amounts = self.coins[:]
        new_amounts[denom_idx] += 1
        new_change = Change(None, new_amounts, len(self.coins))
        return new_change

def making_change_internal(amount, denominations, cache):
    if amount in cache:
        return cache[amount]
    if amount < denominations[0]:
        return set()
    ways = set()
    for denom_idx, denom in enumerate(denominations):
        if amount == denom:
            ways.update([Change(denominations).increment(denom_idx)])
        elif amount > denom:
            ways.update((change.increment(denom_idx) for change in making_change_internal(amount - denom, denominations, cache)))
    cache[amount] = ways
    return ways

making_change_cache = {}
def making_change(amount, denominations):
    global making_change_cache
    if amount <= 0:
        return 1
    return len(making_change_internal(amount, denominations, making_change_cache))


if __name__ == "__main__":
  # Test our your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  if len(sys.argv) > 1:
    denominations = [1, 5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
  else:
    print("Usage: making_change.py [amount]")
