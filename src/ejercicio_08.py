def fibonacci_impares():
    fib = (1, 1)
    while len(fib) < 20:
        fib += (fib[-1] + fib[-2],)
    
    impares = [num for num in fib if num % 2 != 0]
    print("Secuencia Fibonacci:", fib)
    print("Impares:", impares)


fibonacci_impares()
