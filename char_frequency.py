def word_frequency(s):
    freq={}
    for ch in s:
        if ch in freq:
            freq[ch]+=1
        else:
            freq[ch]=1
    return freq
s=input("Enter a String:")
result=word_frequency(s)
for key,value in result.items():
    print(key,":",value)
