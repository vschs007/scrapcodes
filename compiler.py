t = int(input())
for i in range(t):
    s = input()
    ans = 0
    count = 0
    for k in range(len(s)):
        if s[k] == "<":
            count += 1
        elif s[k] == ">":
            count -= 1
        if count < 0:
            break
        elif count == 0:
            ans = max(ans, k + 1)
    print(ans)
