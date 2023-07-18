def getPlanetToDestroy(arr):
    N = len(arr);
    odd = [0] * N;
    even = [0] * N;
    even[0] = arr[0];
    for i in range(1, N):
        odd[i] = odd[i - 1];
        even[i] = even[i - 1];
        if (i % 2 == 0):
            even[i] += arr[i];
        else:
            odd[i] += arr[i];
    find = False;
    p = odd[N - 1];
    q = even[N - 1] - arr[0];
    if (p == q):
        return 1;
        find = True;
    for i in range(1, N):
        if (i % 2 == 0):
            p = even[N - 1] - even[i - 1] - arr[i] + odd[i - 1];
            q = odd[N - 1] - odd[i - 1] + even[i - 1];
        else:
            q = odd[N - 1] - odd[i - 1] - arr[i] + even[i - 1];
            p = even[N - 1] - even[i - 1] + odd[i - 1];
        if (p == q):
            find = True;
            return i+1
    if (find == False):
        return -1

print(getPlanetToDestroy([2,5,3,1]))