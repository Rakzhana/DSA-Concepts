def  only_digit(s):
    for ch in s:
        if ch<'0' or ch>'9':
            return False
    return True
s=input()
if  only_digit(s):
    print("The string contains only digits")
else:
    print("The string does not contain only digits")
