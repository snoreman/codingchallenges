"""
learning fibanacci solutions in dynamic programming
dynamic programming is a way of making your algorim more efficient
by storing some of the intermediate results. 
works well when algorithm has a lot of repetitive computations

fib sequence
1, 2, 2, 3, 5, 8. 13,..

write function to find nth fibannaci number
fib(3) = 2
fib(5) = 5
"""



"""
recursive solution
"""
def fib(n):
    if n== 1 or n == 2:
        result = 1
    else:
        result = fib(n-1) + fib (n-2)
    return result


print (fib(8))


'''
memoized solution
'''

def fib_2(n, memo):
    if memo[n] is not None:
        return memo[n]
    if n == 1 or n == 2:
        result = 1
    else:
        result = fib_2(n-1,memo) + fib_2(n-2, memo)
    memo[n] = result
    return result
def fib_memo(n):
    memo = [None] * (n+1)
    return fib_2(n,memo)

print(fib_memo(35))

def fib_bottom_up(n):
    if n == 1 or n == 2:
        return 1
    bottom_up = [None] * (n+1)
    bottom_up[1] = 1
    bottom_up[2] = 1
    for i in range( 3 , n+1):
        bottom_up[i] = bottom_up[i-1] + bottom_up[i-2]
    return bottom_up[n]

print (fib_bottom_up(35))
