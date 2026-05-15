def union(arr1,arr2):
    uni=[]
    for num in arr1:
        if num not in uni:
            uni.append(num)
    for num in arr2:
        if num not in uni:
            uni.append(num)
    return uni
n=int(input("Enter number of elements in array1"))
arr1=[]
m=int(input("Enter number of elements in array2"))
arr2=[]
for i in range(n):
    arr1.append(int(input()))
for j in range(m):
    arr2.append(int(input()))
print("Union of two array is:", union(arr1,arr2))
