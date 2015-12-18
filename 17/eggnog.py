"""
--- Day 17: No Such Thing as Too Much ---

The elves bought too much eggnog again - 150 liters this time. To fit it all into your refrigerator, you'll need to move
it into smaller containers. You take an inventory of the capacities of the available containers.

For example, suppose you have containers of size 20, 15, 10, 5, and 5 liters. If you need to store 25 liters, there are
four ways to do it:

15 and 10
20 and 5 (the first 5)
20 and 5 (the second 5)
15, 5, and 5
Filling all containers entirely, how many different combinations of containers can exactly fit all 150 liters of eggnog?
"""
from itertools import compress, product


def combinations(items):
    return (list(compress(items, mask)) for mask in product(*[[0, 1]]*len(items)))


combs = combinations([50, 44, 11, 49, 42, 46, 18, 32, 26, 40, 21, 7, 18, 43, 10, 47, 36, 24, 22, 40])
# combs = combinations([20, 15, 10, 5, 5])
print len([comb for comb in combs if sum(comb) == 150 and len(comb) == 4])
