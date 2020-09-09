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


def eating_cookies(n):
    cookie = 0
    #  if too many cookies eaten
    while cookie is < n:

    if cookie > n:
        return 0
    if cookie == n:
        return 1

    return eating_cookies(cookie + 1) + eating_cookies(cookie + 2) + eating_cookies(cookie + 3)

#     # eat 1 cookies, eat 2 cookies, eat 3 cookies


# if __name__ == "__main__":
#     # Use the main function here to test out your implementation
#     num_cookies = 5

#     print(
#         f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")


while j <= len(new_arr):
    if new_arr[i] == new_arr[j]:

        if i != new_arr[- 1]:
            i += 2

        if j != new_arr[- 2]:
            j += 2

        else:
            return new_arr[i]
    else:
        print(new_arr[i])
        return new_arr[i]
