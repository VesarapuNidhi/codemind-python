def isPerfectSquare(num):
    if num < 0:
        return False
    if num == 0 or num == 1:
        return True
    start = 1
    end = num
    while start <= end:
        mid = (start + end) // 2
        square = mid * mid

        if square == num:
            return True
        elif square < num:
            start = mid + 1
        else:
            end = mid - 1

    return False
def process_test_cases():
    num_tests = int(input())
    results = []
    for _ in range(num_tests):
        num = int(input())
        results.append(isPerfectSquare(num))
    return results
results = process_test_cases()
for result in results:
    print(result)