def climbStairs(n: int) -> int:
    if n <= 2:
        return n

    dp = [0] * (n + 1)
    dp[1] = 1  # One way to climb 1 stair
    dp[2] = 2  # Two ways to climb 2 stairs

    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


print(climbStairs(4))