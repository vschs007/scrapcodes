n = 8

total = 0
a = [None for i in range(0, n+1)]
s = []
p = 1
while (p < n):
  p = p + 1

  if a[p] is None:
    a[p] = p - 1
    total = total + a[p]
    s.append(p)

    limit = n / p
    new_s = []

    for i in s:
      j = i
      while j <= limit:
        new_s.append(j)
        a[j * p] = a[j] * p if (not j % p) else a[j] * (p-1)
        total = total + a[j * p]
        j = j * p
    s = new_s

print(total)