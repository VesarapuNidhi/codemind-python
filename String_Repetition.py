def count_a_in_infinite_string(s, n):
    a_count_in_s = s.count('a')
    complete_repetitions = n // len(s)
    remaining_characters = n % len(s)
    a_count_in_remaining = s[:remaining_characters].count('a')
    total_a_count = (complete_repetitions * a_count_in_s) + a_count_in_remaining
    return total_a_count
s = input().strip()
n = int(input().strip())
result = count_a_in_infinite_string(s, n)
print(result)