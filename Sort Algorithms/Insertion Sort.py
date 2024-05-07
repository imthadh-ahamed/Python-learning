# Create an empty list to store the numbers
arr = []

# Loop to get 7 numbers from the user and add them to the list
for i in range(7):
    arr.append(int(input("Enter a number: ")))

# Print the entered numbers
print("Entered numbers: ", arr)

# Define a function to perform insertion sort on the given array
def insertionSort(arr):
    #Initialize the length of array
    n = len(arr)
    # Iterate over the array starting from the second element
    for i in range(1, n):
        # Store the current element as the key
        key = arr[i]
        # Initialize a variable to track the index of the element before the current element
        j = i - 1
        # Move elements of arr[0..i-1], that are greater than key, to one position ahead of their current position
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j = j - 1
        # Place the key at its correct position in the sorted array
        arr[j+1] = key



def insertionSort2(arr):
    n = len(arr)
    for i in range(1, n):
        j = i
        while arr[j - 1] > arr[j]:
            arr[j-1], arr[j] = arr[j], arr[j-1]
            j = j - 1



# Call the insertionSort function to sort the array
insertionSort(arr)
# Print the sorted array
print("Sorted array: ", arr)


# Call the insertionSort2 function to sort the array
insertionSort2(arr)
# Print the sorted array
print("Sorted array 2: ", arr)
