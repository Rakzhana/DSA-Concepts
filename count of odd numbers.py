def countodd(arr):
    count=0
    for num in arr:
        if(num%2==1):
            count+=1
    return count
print("Enter the size of the array")
n=int(input())
arr=[]
for i in range(n):
    print("Enter the value for the array")
    arr.append(int(input()))
print("Number of odd numbers in the array is:",countodd(arr))
