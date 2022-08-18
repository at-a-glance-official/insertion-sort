def insertion_sort(arr):
    for chief in range(1,len(arr)):
        while arr[chief] < arr[chief-1] and chief > 0:
            arr[chief], arr[chief-1] = arr[chief-1], arr[chief] # swap
            chief -= 1

    return arr

arr = [20,1,21,4,3,212,-1223,10000,-5456]
print(insertion_sort(arr))