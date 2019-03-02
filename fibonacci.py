def fib(n):
    global c
    c += 1
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)
    
c = 0
print(fib(6), "Iterations: ", c)
