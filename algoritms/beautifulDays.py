def beautifulDays(i, j, k):
    out=0
    for day in range(i, j+1):
        revday=int(str(day)[::-1])
        res = abs(day - revday)
        if res % k ==0 :out = out+1
    return out