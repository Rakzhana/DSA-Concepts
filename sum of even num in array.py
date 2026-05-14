def sumeven(arr):
    s=0
    for num in arr:
        if (num%2==0):
            s+=num
    return s
print("Enter the size of the array")
n=int(input())
arr=[]
for i in range(n):
    print("Enter the value for array")
    arr.append(int(input()))
print("The sum of even numbers in the array is:",sumeven(arr))
