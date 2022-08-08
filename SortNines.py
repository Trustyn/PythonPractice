
def reorder(arr):
    count = 0
    for i in arr:
        if(i == 9):
            arr.remove(i)
            count += 1
    for i in range(count):
        arr.append(9)
    return arr


arr = [1,3,9,0,2,9,9,2,4,9]
print(reorder(arr))