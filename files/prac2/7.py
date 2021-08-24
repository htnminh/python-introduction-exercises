def sum_of_digit(n):
    if n <= 9:
        return n
    return sum_of_digit(n//10) + n % 10 