#sử dụng một trong các hàm sắp xếp sau:
# nổi bọt
def bubbleSort(arr):
    def swap(i, j):
        arr[i], arr[j] = arr[j], arr[i]
    n = len(arr)
    swapped = True    
    x = -1
    while swapped:
        swapped = False
        x = x + 1
        for i in range(1, n-x):
            if arr[i - 1] > arr[i]:
                swap(i - 1, i)
                swapped = True                    
    return arr
#sắp xếp chọn
def selectionSort(arr):        
    for i in range(len(arr)):
        minimum = i        
        for j in range(i + 1, len(arr)):           
            if arr[j] < arr[minimum]:
                minimum = j       
        arr[minimum], arr[i] = arr[i], arr[minimum]            
    return arr
#sắp xếp chèn
def insertionSort(arr):        
    for i in range(len(arr)):
        cursor = arr[i]
        pos = i        
        while pos > 0 and arr[pos - 1] > cursor:          
            arr[pos] = arr[pos - 1]
            pos = pos - 1       
        arr[pos] = cursor
    return arr
#Sắp xếp trộn
def mergeSort(arr):  
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2   
    left, right = mergeSort(arr[:mid]), mergeSort(arr[mid:])    
    return merge(left, right, arr.copy())
def merge(left, right, merged):
    left_cursor, right_cursor = 0, 0
    while left_cursor < len(left) and right_cursor < len(right):    
     
        if left[left_cursor] <= right[right_cursor]:
            merged[left_cursor+right_cursor]=left[left_cursor]
            left_cursor += 1
        else:
            merged[left_cursor + right_cursor] = right[right_cursor]
            right_cursor += 1            
    for left_cursor in range(left_cursor, len(left)):
        merged[left_cursor + right_cursor] = left[left_cursor]        
    for right_cursor in range(right_cursor, len(right)):
        merged[left_cursor + right_cursor] = right[right_cursor]
    return merged
#quick sort
def partition(array, begin, end):
    pivot_idx = begin
    for i in range(begin+1, end+1):
        if array[i] <= array[begin]:
            pivot_idx += 1
            array[i], array[pivot_idx] = array[pivot_idx], array[i]
    array[pivot_idx], array[begin] = array[begin], array[pivot_idx]
    return pivot_idx
def quick_sort_recursion(array, begin, end):
    if begin >= end:
        return
    pivot_idx = partition(array, begin, end)
    quick_sort_recursion(array, begin, pivot_idx-1)
    quick_sort_recursion(array, pivot_idx+1, end)
def quick_sort(array, begin=0, end=None):
    if end is None:
        end = len(array) - 1    
    return quick_sort_recursion(array, begin, end)
f=open("b1-anhca.inp")
n=list(map(lambda x:int(x),f.readline().strip()))
f.close()
print(n)
# sắp xếp
bubbleSort(n)
#n.reverse()  một là sử dụng cái này để  đảo ngược lại thứ tự, hai là sư dụng n[::-1]
print(n)
#ghi file
f=open("b1-anhca.out","w",encoding="UTF8")
f.write("".join(list(map(lambda x:str(x),n[::-1]))))
f.close()