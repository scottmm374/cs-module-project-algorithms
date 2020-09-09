'''
Input: an integer
Returns: an integer
'''


def climb_stairs(current, desired):
    if current > desired:
        return 0
    if current == desired:
        return 1

    return climb_stairs(current + 1, desired) + climb_stairs(current + 2, desired) + climb_stairs(current + 3, desired)


x = climb_stairs(0, 3)
print(x)


# def eating_cookies(n):
#     eat_cookies = randint(1, 3)
#     cookie = 0
#     ways_to_eat = 0
#     #  if too many cookies eaten
#     while cookie is < n:

#         if cookie > n:
#             return 0
#         if cookie == n:
#             ways_to_eat += 1


#     # eat 1 cookies, eat 2 cookies, eat 3 cookies


# if __name__ == "__main__":
#     # Use the main function here to test out your implementation
#     num_cookies = 5

#     print(
#         f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
