def partition(arr, l, h):
    pivot = arr[l]
    i = l + 1
    j = h
    while True:
       
        while i <= h and arr[i] < pivot:
            i += 1
   
        while j >= l and arr[j] > pivot:
            j -= 1
        
        if i >= j:
            break
        # Swap elements
        arr[i], arr[j] = arr[j], arr[i]
    
    
    arr[l], arr[j] = arr[j], arr[l]
    return j

def quicksort(arr, l, h):
    if l < h:
        j = partition(arr, l, h)
        quicksort(arr, l, j - 1)
        quicksort(arr, j + 1, h)

def print_array(arr):
    for i in arr:
        print(i, end=" ")
    print()

if __name__ == "__main__":
    arr = [11,24,83,4,36]
    print("Given array is:", arr)
    quicksort(arr, 0, len(arr) - 1)
    print("Sorted array is:", end=" ")
    print_array(arr)
