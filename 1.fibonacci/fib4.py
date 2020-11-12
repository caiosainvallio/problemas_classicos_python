from functools import lru_cache

@lru_cache(maxsize=None)
def fib4(n: int) -> int: # mesma definição de fib2
    if n < 2: # caso de base
        return n
    return fib4(n -2) + fib4(n -1) # caso recursivo

if __name__ == '__main__':
    print(fib4(5))
    print(fib4(50))
