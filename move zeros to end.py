def movezer(arr):
    res=[]
    for i in arr:
        if i !=0:
            res.append(i)
        zero_count=len(arr)-len(res)
    for j in range(zero_count):
        res.append(0)
    return res

n=int(input())
arr=[]
for i in range(n):
    arr.append(int(input()))
print("Array after moving all zeros to the end",movezer(arr))
