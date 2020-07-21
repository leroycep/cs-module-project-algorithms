'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Find the last nonzero number in the array
    nonzero_index = len(arr) - 1
    while arr[nonzero_index] == 0:
        nonzero_index -= 1
        # The entire right side of the array is zeroes,
        # we don't need to do anything else
        if nonzero_index == 0:
            return arr

    for i in range(len(arr)):
        if i >= nonzero_index:
            break
        if arr[i] == 0:
            arr[i] = arr[nonzero_index]
            arr[nonzero_index] = 0
            while arr[nonzero_index] == 0:
                nonzero_index -= 1
    return arr

if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 0, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
