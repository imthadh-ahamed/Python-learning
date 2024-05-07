arr = []
for i in range(7):
    arr.append(int(input("Enter a number: ")))
    
print("Enterd numbers: ", arr)

def bubbleSort(arr):
    n = len(arr)
    for a in range(n):
        for b in range(0, n-a-1):
            if(arr[b] > arr[b+1]):
                arr[b], arr[b+1] = arr[b+1], arr[b]

bubbleSort(arr)
print("Sorted array: ", arr)