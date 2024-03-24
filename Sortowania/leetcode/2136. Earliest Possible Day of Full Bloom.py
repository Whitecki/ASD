# You have n flower seeds. Every seed must be planted first before it can begin to grow, then bloom. Planting a seed takes
# time and so does the growth of a seed. You are given two 0-indexed integer arrays plantTime and growTime, of length n each:
#
#     plantTime[i] is the number of full days it takes you to plant the ith seed. Every day, you can work on planting
# exactly one seed. You do not have to work on planting the same seed on consecutive days, but the planting of a seed is
# not complete until you have worked plantTime[i] days on planting it in total.
#     growTime[i] is the number of full days it takes the ith seed to grow after being completely planted. After the last
# day of its growth, the flower blooms and stays bloomed forever.
#
# From the beginning of day 0, you can plant the seeds in any order.
# Return the earliest possible day where all seeds are blooming.

def earliestFullBloom(plantTime, growTime):
    n = len(growTime)
    growTime = [(growTime[i],i) for i in range(n)]
    growTime.sort(key= lambda x: x[0])
    base = growTime[0][0] + plantTime[growTime[0][1]]
    for i in range(1,n):
        if growTime[i][0] > base:
            base += (growTime[i][0] - base)
        base += plantTime[growTime[i][1]]
    return base

plantTime = [1,4,3]
growTime = [2,3,1]
print(earliestFullBloom(plantTime,growTime))
