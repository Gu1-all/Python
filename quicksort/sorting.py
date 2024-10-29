def quicksort(arr, esq, dir):
    if esq < dir:
        particao_pos = particao(arr, esq, dir)
        quicksort(arr, esq, particao_pos - 1)
        quicksort(arr, particao_pos + 1, dir)

def particao(arr, esq, dir):
    i = esq
    j = dir - 1
    pivot = arr[dir] 

    while i < j:
        while i < dir and arr[i] < pivot:
            i += 1
        while j > esq and arr[j] >= pivot:
            j -= 1
        
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    
    if arr[i] > pivot:
        arr[i], arr[dir] = arr[dir], arr[i]
    
    return i

arr = [22, 11, 10, 100, 99, 88]
quicksort(arr, 0, len(arr) - 1)
print(arr)