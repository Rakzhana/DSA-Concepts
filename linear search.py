def linear(arr,key):
    for i in range(len(arr)):
        if arr[i]==key:
            return i
    return -1
n=int(input())
arr=[]
for i in range(n):
    arr.append(int(input()))
key=int(input("Enter the element to search:"))
result=linear(arr,key)
if result!=-1:
    print("Element found at index:",result)
else:
    print("Element not found")
