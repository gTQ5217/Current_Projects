def digit_frequency(n):
    frequency_map = {}
    while n > 0:
        digit = n % 10
        if digit in frequency_map:
            frequency_map[digit] += 1
        else:
            frequency_map[digit] = 1
        n //= 10
    return frequency_map