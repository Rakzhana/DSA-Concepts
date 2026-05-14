def second(arr):
    largest=second=float('-inf')
    for num in arr:
        if num>largest:
            second=largest
            largest=num
        elif num>second and num!=largest:
            second=num
    return second
m=int (input())
arr=[]
for i in range(m):
    arr.append(int(input()))
print("Second Largest Element in the array is:", second(arr))
