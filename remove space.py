def remove(s):
    result=" "
    for ch in s:
        if ch !=" ":
            result+=ch
    return result;
s=input("Enter a string:")
print(remove(s))
