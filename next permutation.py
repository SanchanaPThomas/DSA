def nextPermutation(arr):
    n = len(arr)

    # STEP 1: find the pivot (first element from right that is smaller than next)
    i = n - 2
    while i >= 0 and arr[i] >= arr[i + 1]:
        i -= 1

    # STEP 2: if pivot exists, find just larger element and swap
    if i >= 0:
        j = n - 1
        while arr[j] <= arr[i]:
            j -= 1
        arr[i], arr[j] = arr[j], arr[i]

    # STEP 3: reverse the right part
    arr[i + 1:] = reversed(arr[i + 1:])

    return arr
