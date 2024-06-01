def mergeSort(arr):
    # If the array has more than one element
    if len(arr) > 1:
        # Find the middle point and divide the array into two halves
        mid = len(arr) // 2
        left_arr = arr[:mid]  # Left half
        right_arr = arr[mid:]  # Right half

        # Recursively sort the left half
        mergeSort(left_arr)
        # Recursively sort the right half
        mergeSort(right_arr)

        # Initialize indices for left, right, and merged arrays
        i = 0  # Index for left array
        j = 0  # Index for right array
        k = 0  # Index for merged array

        # Merge the two halves
        while i < len(left_arr) and j < len(right_arr):
            # Compare elements from left and right arrays and merge them in sorted order
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1

        # Copy any remaining elements of the left array (if any)
        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1

        # Copy any remaining elements of the right array (if any)
        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1


# Sample usage
arr = [2, 8, 7, 1, 3, 5, 6, 4]
mergeSort(arr)
print("Sorted array: ", arr)
