#Given an int arr[] and the kth element (int k) locate the Kth 
#largest value in the array i.e. [2, 10, 1, 5] k = 2 
#output = 0 index : k = 3 output = 3 index

def locateValue(arr, k):
    for i in arr.sort():
        return i[k] 




arr = [2, 10, 1, 5]
k = 2
print(arr)
print(k)
print(locateValue(arr, k))