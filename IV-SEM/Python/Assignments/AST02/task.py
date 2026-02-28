def even_odd(n: int) -> str:
    if n % 2 != 0:   # If n is odd
        return "Weird"
    else:  # If n is even
        if 2 <= n <= 5:
            return "Not Weird"
        elif 6 <= n <= 20:
            return "Weird"
        else:  # n > 20
            return "Not Weird"


if __name__ == '__main__':
    n = int(input())
    print(even_odd(n))