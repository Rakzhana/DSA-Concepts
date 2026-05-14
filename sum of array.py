def arrsum(arr):
    s=0
    for num in arr:
        s+=num
    return s
print("Enter the size of array:")
n=int(input())
arr=[]
for i  in range(n):
    print("Enter the values of the array")
    arr.append(int(input()))
print("The sum of the array is:",arrsum(arr))
    
