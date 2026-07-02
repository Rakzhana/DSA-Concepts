def non_repeating_char(s):
    for ch in s:
        if s.count(ch)==1:
            return ch
    return "No non-repeating characters found"
s=input()
print(non_repeating_char(s))
