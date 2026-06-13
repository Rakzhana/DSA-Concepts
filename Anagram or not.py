def anagram(s1,s2):
    if sorted(s1)==sorted(s2):
        return True
    return False
s1=input("Enter a string:")
s2=input("Enter a string: ")
if(anagram(s1,s2)):
   print("Anagram")
else:
    print("Not Anagram")
