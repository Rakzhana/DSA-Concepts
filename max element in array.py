def large(arr):
    max=arr[0]
    for num in arr:
        if num>max:
            max=num
    return max
print("Enter the size of array:")
n=int(input())
arr=[]
for i in range(n):
    print("Enter the array values")
    arr.append(int(input()))
print("Largest value in array:", large(arr))

    
