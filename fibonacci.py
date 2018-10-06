# find the nth fibonacci number
# recursive solution - TIME COMPLEXITY - O(2^n/2)[T(n-1) + T(n-2)]
def fib(n):
    # base case
    if n <=2 : 
        f=1 # return 1
    else:
        f = fib(n-1) + fib(n-2) # return fib(n-1) + fib(n-2)
    return f

# Improvement is to add memoization create an empty dict
# before the computation, check if the val is in dict
# memoized calls only cost constant time , hence time - O(n)
memo = {}
def fib(n):
    if n in memo:
        return memo[n]
    # base case
    if n <=2 : 
        f=1 # return 1
    else:
        f = fib(n-1) + fib(n-2) # return fib(n-1) + fib(n-2)
    memo[n] = f
    return memo[n]
# best algo to solve fibonacci -O(log n) =>
# DP - divide and store the problems into subproblems- recursion + memoization
# DP TC == #Subproblems * time/subproblems
#DP - 1)topdown  2) Bottomdown

#Bottom up Fib
def fib_bottom_up(n):
    fib = {}
    for k in range(n):
        if k<=2 :
            f = 1
        else:
            f = fib[k-1] + fib[k-2]
        fib[k] = f
    return fib[n]
