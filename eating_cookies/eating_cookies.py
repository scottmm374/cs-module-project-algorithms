'''
Input: an integer
Returns: an integer
'''


# def climb_stairs(current, desired):
#     print(current)
#     if current > desired:
#         return 0
#     if current == desired:
#         return 1

#     return climb_stairs(current + 1, desired) + climb_stairs(current + 2, desired)

def climb_stairs(current, desired, cache={}):
    if current > desired:
        return 0
    if current == desired:
        return 1
    if current not in cache:
        cache[current] = climb_stairs(
            current + 1, desired, cache) + climb_stairs(current + 2, desired, cache)
    return cache[current]


climb_stairs(0, 5)


# def eating_cookies(n):
#     cookies = 0
#     while cookies <= n:
#         cookies = randint(1, 3)
#     ways_to_eat = 0
#     if cookie > n:
#         return 0
#     if cookie <= n:
#         return eat_cookies
#         ways_to_eat += 1


#     # eat 1 cookies, eat 2 cookies, eat 3 cookies


# if __name__ == "__main__":
#     # Use the main function here to test out your implementation
#     num_cookies = 5

#     print(
#         f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
