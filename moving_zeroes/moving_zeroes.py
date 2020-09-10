'''
Input: a List of integers
Returns: a List of integers
'''


def moving_zeroes(arr):
    # non_zero = 0
    i = 0
    while i < (len(arr)):

        if arr[i] != 0:
            # non_zero += 1
            i += 1
        else:
            # zero = i
            zero = arr.pop(i)
            # print(zero, "zero")
            arr.append(zero)
            i += 1
            # print(arr, "print array")

    return(arr)


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
# moving_zeroes(arr)
