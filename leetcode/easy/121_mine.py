# 121. Best Time to Buy and Sell Stock

import sys

# Example 1:
# Input:
# prices = [7, 1, 5, 3, 6, 4]
# Output: 5

# Input:


prices = [1, 6, 9, 0, 6, 1, 7]


output = 0

minPrice = sys.maxsize

for price in prices:
    minPrice = min(price, minPrice)
    output = max(output, price - minPrice)

output


