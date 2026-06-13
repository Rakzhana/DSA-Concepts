def case(s):
  result=" "
  for ch in s:
    if 'a'<=ch<='z':
      result+=chr(ord(ch)-32)
    else:
      result+=ch
   return result
 s=input("Enter a string:")
print(case(s))
  
