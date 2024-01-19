#bubble sort

def bubblesort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j] = arr[j+1]
                arr[j+1] = arr[j]

                return arr
        
arr = [5,3,8,6,7,2]
print(bubblesort(arr))