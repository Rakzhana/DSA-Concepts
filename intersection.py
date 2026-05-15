def intersection(arr1,arr2):
    intersection=[]
    for num in arr1:
        if num in arr2 and num not in intersection:
            intersection.append(num)
    return intersection
n=int(input("Enter the size of the first array: "))
arr1=[]
for i in range(n):
    arr1.append(int(input()))
m=int(input("Enter the size of the second array:"))
arr2=[]
for  j in range(m):
    arr2.append(int(input()))
print("Intersection on two arrays:",intersection(arr1,arr2))
