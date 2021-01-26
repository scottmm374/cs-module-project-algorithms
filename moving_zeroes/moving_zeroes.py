'''
Input: a List of integers
Returns: a List of integers
'''

#  Find middle and put on each side


def moving_zeroes(arr):
    z_arr = []
    arr_length = len(arr)
    i = 0
    while i <= (arr_length - 1):

        if arr[i] != 0:
            i += 1
        else:
            zero = arr.pop(i)
            z_arr.append(zero)
            arr_length -= 1
            # i += 1
    for i in z_arr:
        arr.append(i)
        print(arr)
    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 0, 0, 0, 3, 2, 1]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
# moving_zeroes(arr)
