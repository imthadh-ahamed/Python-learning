# Create an empty list to store the numbers
arr = []

# Loop to get 7 numbers from the user and add them to the list
for i in range(7):
    arr.append(int(input("Enter a number: ")))
    
# Print the entered numbers
print("Entered numbers: ", arr)

# Define a function to perform bubble sort on the given array
def bubbleSort(arr):
    #Initialize the length of array
    n = len(arr)
    # Outer loop to traverse the array
    for a in range(n):
        # Inner loop to iterate over the unsorted part of the array
        for b in range(0, n-a-1):
            # Compare adjacent elements and swap them if they are in the wrong order
            if(arr[b] > arr[b+1]):
                arr[b], arr[b+1] = arr[b+1], arr[b]

# Call the bubbleSort function to sort the array
bubbleSort(arr)

# Print the sorted array
print("Sorted array: ", arr)
