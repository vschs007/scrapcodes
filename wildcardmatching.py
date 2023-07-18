s = "acdcb"
p = "a*c?b"


# ? any single character, * any sequence of char

if '*' not in p and len(p) != len(s):
    print("false")
else:
    for i, k in zip(p, s):
        if i == s or i == '?' or i==k:
            continue
        elif i == '*':
            print("true")
            break
        else:
            print("false")
            break