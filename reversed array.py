def rev(arr):
    rev=[]
    for i in range(len(arr)-1,-1,-1):
        rev.append(arr[i])
    return rev
n=int(input())
arr=[]
for i in range(n):
    arr.append(int(input()))
print("Original Array:", arr)
print("Reversed  Array:",rev(arr))
