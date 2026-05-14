def removedup(arr):
    unique=[]
    for num in arr:
        if num not in unique:
            unique.append(num)
    return unique
n=int(input())
arr=[]
for i in range(n):
    arr.append(int(input()))
print("Array after removing duplicates:",removedup(arr))
