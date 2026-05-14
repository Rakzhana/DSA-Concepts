def small(arr):
    mini=arr[0]
    for num in arr:
        if num<mini:
            mini=num
    return mini
print("Enter the number of elements in the array:")
n=int(input())
arr=[]
for i in range(n):
    print("Enter the array values")
    arr.append(int(input()))
print("Smallest emlemnt in the array:",small(arr))
