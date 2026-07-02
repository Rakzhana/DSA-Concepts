def first_repeating_char(s):
    visited=[]
    for ch in s:
        if ch in visited:
            return ch
        visited.append(ch)
    return "No repeating characters"
s=input()
print(first_repeating_char(s))
