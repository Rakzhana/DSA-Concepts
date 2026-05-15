def missing(arr):
    total=n*(n+1)//2
    arr_sum=sum(arr)
    return total-arr_sum
n=int(input())
arr=[]
print("Enter",n-1,"elements:")
for i in range(n-1):
    arr.append(int(input()))
print("Missing number is:",missing(arr))
