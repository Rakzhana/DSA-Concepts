def rightrotate(arr):
    last=arr[-1]
    for i in range(len(arr)-1,0,-1):
        arr[i]=arr[i-1]
    arr[0]=last
    return arr
n=int(input())
arr=[]
for i in range(n):
    arr.append(int(input()))
print("Array after right rotate:",rightrotate(arr))
