def issorted(arr):
    for i in range(len(arr)-1):
        if (arr[i]>arr[i+1]):
            return False
    return True
n=int(input())
arr=[]
for i in range(n):
    arr.append(int(input()))
if issorted(arr):
    print("Array is sorted")
else:
    print("Array is not sorted")
