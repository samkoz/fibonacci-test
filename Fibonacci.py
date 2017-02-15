#Fibonacci Algorithm

def fibonacci(n):
    fib_list = []
    a = 0;
    b = 1;
    while n > 1:
        fib_list.append(a)
        a, b = b, a + b
        n = n - 1
    fib_list.append(a);
    print(fib_list, len(fib_list))
    return a

if __name__ == "__main__":
    print(fibonacci(10))
