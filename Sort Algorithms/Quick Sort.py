def quickSort(arr, l, r):
    # If the subarray has more than one element
    if l < r:
        # Partition the array and get the pivot index
        part = partition(arr, l, r)
        # Recursively sort the left part of the array
        quickSort(arr, l, part - 1)
        # Recursively sort the right part of the array
        quickSort(arr, part + 1, r)


def partition(arr, l, r):
    # Choose the pivot as the last element in the array
    pivot = arr[r]
    # Index of the smaller element
    i = l - 1

    # Traverse through all elements in the subarray except the pivot
    for j in range(l, r):
        # If the current element is smaller than or equal to the pivot
        if arr[j] < pivot:
            # Increment the index of the smaller element
            i += 1
            # Swap the current element with the element at index i
            arr[i], arr[j] = arr[j], arr[i]

    # Swap the pivot element with the element at index i+1
    arr[i + 1], arr[r] = arr[r], arr[i + 1]
    # Return the index of the pivot element
    return i + 1


# Sample usage
arr = [2, 8, 7, 1, 3, 5, 6, 4]
low = 0
high = len(arr) - 1

# Call quickSort on the entire array
quickSort(arr, low, high)

# Print the sorted array
print("Sorted array :", arr)
