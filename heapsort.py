def maxheapify(arr,n,i):
    largest = i
    left = 2*i+1
    right = 2*i+2
    if left<n and arr[left]<arr[largest]:
        largest = left
    if right<n and arr[right]<arr[largest]:
        largest = right
    if largest != i:
        temp = arr[i]
        arr[i] = arr[largest]
        arr[largest] = temp
        maxheapify(arr,n,largest)

def maxHeapSort(arr,n):
    for i in range((n//2)-1,-1,-1):
        maxheapify(arr,n,i)
    for i in range(n-1,-1,-1):
        temp = arr[0]
        arr[0] =arr[i]
        arr[i] = temp
        maxheapify(arr,i,0)   
    return arr

def minheapify(arr,n,i):
    minimum = i
    left = 2*i+1
    right = 2*i+2
    if left<n and arr[left]>arr[minimum]:
        minimum = left
    if right<n and arr[right]>arr[minimum]:
        minimum = right
    if minimum != i:
        temp = arr[i]
        arr[i] = arr[minimum]
        arr[minimum] = temp
        minheapify(arr,n,minimum)

def minHeapSort(arr,n):
    for i in range((n//2)-1,-1,-1):
        minheapify(arr,n,i)
    for i in range(n-1,-1,-1):
        temp = arr[0]
        arr[0] =arr[i]
        arr[i] = temp
        minheapify(arr,i,0)   
    return arr

