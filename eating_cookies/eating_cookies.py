'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n, cache=None):
    if cache and cache[n] != 0:
        return cache[n]
    if n <= 0:
        return 1
    if n == 1:
        return 1
    if n == 2:
        return 2
    else:
        if cache is None:
            cache = [0] * (n + 1)
        result = eating_cookies(n - 3, cache) + eating_cookies(n - 2, cache) + eating_cookies(n - 1, cache)
        cache[n] = result
        return result

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
