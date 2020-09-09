'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''


# def single_number(arr):
#     new_arr = arr
#     for i in arr:

#         if not arr.index(i):
#             print(arr.index(i))
#             return i


def single_number(arr):
    new_arr = sorted(arr)

    i = 0
    j = 1

    while i <= len(new_arr):
        if new_arr[i] == new_arr[j]:
            # print(new_arr[i], new_arr[j])
            i += 2
            if j != new_arr[- 2]:
                j += 2
            # elif j == new_arr[-2]:
            #     i += 2
            else:
                return new_arr[-2]
        else:
            # print(new_arr[i])
            return new_arr[i]


#  Passes half the time, sometimes gets stuck on 500
if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 1, 4, 4, 5, 5, 3, 3, 9]
    # arr = [0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 9, 9, 10, 10,
    #    11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 16, 16, 17, 17, 18, 18, 19]

    print(single_number(arr))
# single_number(arr)


# while j <= len(new_arr):
#         if new_arr[i] == new_arr[j]:

#             if i != new_arr[- 1]:
#                 i += 2

#             if j != new_arr[- 2]:
#                 j += 2

#             else:
#                 return new_arr[i]
#         else:
#             print(new_arr[i])
#             return new_arr[i]
