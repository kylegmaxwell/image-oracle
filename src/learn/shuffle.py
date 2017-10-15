import random

def shuffle(arr):
    random.seed(0)
    for s in range(0,7):
        for i in range(0,len(arr)-1):
            # print(str(i)+' '+str(random.randint(i,len(arr)-1)))
            idx = random.randint(i,len(arr)-1)
            tmp = arr[i]
            arr[i] = arr[idx]
            arr[idx]=tmp