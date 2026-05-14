def binarysearch(arr,key):
    low=0
    high=len(arr)-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==key:
            return mid
        elif arr[mid]<key:
            low=mid+1
        else:
            high=mid-1
    return -1
n=int(input())
arr=[]
for i in range(n):
    arr.append(int(input()))
key=int(input("Enter the key to find"))
result=binarysearch(arr,key)
if result!=-1:
    print("The value found at:",result)
else:
    print("The value not found")
