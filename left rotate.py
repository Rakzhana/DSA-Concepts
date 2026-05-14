def leftrotate(arr):
    first=arr[0]
    for i in range(len(arr)-1):
        arr[i]=arr[i+1]
    arr[-1]=first
    return arr
n=int(input())
arr=[]
for i in range(n):
    arr.append(int(input()))
print("Array after left rotation:",leftrotate(arr))
