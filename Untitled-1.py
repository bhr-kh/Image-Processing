def foo(n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return foo(n // 2)
    else:
        return foo(n // 2) + foo(n // 2 + 1)
    
print(foo(10))