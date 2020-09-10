'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''


def single_number(arr):

    arr.sort()

    i = 0
    j = 1

    while i <= (len(arr)):
        # Run this is i and j values match
        if arr[i] == arr[j]:
            # Keeping track of index, since J gets out of range (odd number list)
            # If j index is not 2nd to last increment both I and J 2 indicies
            if j != (len(arr)-2):
                i += 2
                j += 2

            # If J is second to last index (cannot move anymore), so only increment I (which will default last index)
            else:
                i += 2
            # If i in last index by default because of sort it will be the odd one out we are looking for
                return arr[i]
        # If I and J values do not match before the end of list, we have found the single number, which will always be I because of sort.
        else:
            return arr[i]


#  Passes half the time, sometimes gets stuck on 500
if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    # print(f"The odd-number-out is {single_number(arr)}")
single_number(arr)
