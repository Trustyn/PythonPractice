#Each waffle iron takes 5min. If given a list of times (in minutes after breakfast starts)
#of when each guest shows up, determine how many waffle irons you need to put
#out so that no one has to wait to start their waffles.
#Example: [0,3,3,7,9,10,11,20,23,25]
#Minimum number of waffle irons required = 4

def WaffleIrons(arr):
    count = 0
    temp = []
    for i in range(len(arr)):
        if(len(temp) > 0 and arr[i] >= temp[0]):
            del temp[0]
            temp.append(arr[i] + 5)
        else:
            temp.append(arr[i] + 5)
            count = max(count,len(temp))
    return count
            
    
arr = [0,3,3,7,9,10,11,20,23,25]
print(WaffleIrons(arr))