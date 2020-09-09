'''
Input: a List of integers
Returns: a List of integers
'''


def moving_zeroes(arr):
    count = 0

    for i in range(len(arr)):
        if arr[i] != 0:
            count += 1
        else:
            # zero = i
            zero = arr.pop(i)
            print(zero, "zero")
            arr.append(zero)
            print(arr, "print array")

    return(arr, count)


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 12, -2, 4, 0, 17]

    # print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
moving_zeroes(arr)
