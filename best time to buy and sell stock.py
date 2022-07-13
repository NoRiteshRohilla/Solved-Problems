def solve(n, prices):
    maxprofit = 0
    minpricetillnow = 9999999
    for price in prices:
        maxprofit = max(maxprofit, price - minpricetillnow)
        minpricetillnow = min(minpricetillnow, price)
    return maxprofit
