import random

def shuffle(arr):

    random.seed(0)

    index = list(range(0,len(arr)))
    for s in range(0,7):
        for i in range(0,len(arr)-1):
            # print(str(i)+' '+str(random.randint(i,len(arr)-1)))
            idx = random.randint(i,len(arr)-1)
            swap(arr,i,idx)
            swap(index,i,idx)
    return index

def swap(arr, i, j):
    tmp    = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp