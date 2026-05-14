def frequency(arr):
    visited=[]
    for num in arr:
        if num not in visited:
            count=0
            for x in arr:
                if x==num:
                    count+=1
            print(num,"occurs",count,"times")
            visited.append(num)
n=int(input())
arr=[]
for i in range(n):
    arr.append(int(input()))
frequency(arr)
