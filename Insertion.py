#  Insertion Sort

def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

#print array of size n
def printArray(arr):
    for i in range(len(arr)):
        print(arr[i],end=" ")
    print()

if __name__ == "_main_":
    arr = [12,9,8,14,4]
    insertionSort(arr)
    printArray(arr)