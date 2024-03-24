# https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/resources/mit6_006s20_prob8sol/

#Tim the Beaver needs to study for exams, but it’s getting warmer, and Tim wants to spend more time outside.
# Tim enjoys being outside more when the weather is warmer: specifically, if the temperature outside is t
# integer units above zero, Tim’s happiness will increase by t after spending the day outside (with a decrease
# in happiness when t is negative). On each of the n days until finals, Tim will either study or play outside
# (never both on the same day). In order to stay on top of coursework, Tim resolves never to play outside more
# than two days in a row. Given a weather forecast estimating temperature for the next n days, describe an
# O(n)-time dynamic programming algorithm to determine which days Tim should study in order to increase
# happiness the most.

def Sunny_studies(T:"the temperature on day i"):
    n = len(T)
    dp = [-1 for _ in range(n+1)] #the maximum happiness increase possible during days 0 to i
    #base case
    dp[0],dp[1] = 0, T[0]
    for i in range(2,n+1): # topological order
        dp[i] = max(dp[i-2] + T[i-1], dp[i-1]) # relate
    return dp[n]

T = [1,5,7,2,2,3,9,7]

print(Sunny_studies(T))
