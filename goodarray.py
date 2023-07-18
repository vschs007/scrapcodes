def checkfull(arr, ranges):
    dct = {}
    # flag = True
    for k in ranges:
        substr = arr[k[0]-1:k[1]]
        for ch in substr:
            if ch != "_":
                if ch not in dct:
                    dct[ch] = 1
                else:
                    return False
            else:
                continue
    return True


def goodString(N, Q, S, arr, ranges):
    if len(S)==len(set(S)):
        return 0

    for i in range(len(S)):
        S = list(S)
        for i in range(len(ranges)):
            if "".join(S)[ranges]:
                pass
        S[arr[i] - 1] = "_"
        if checkfull("".join(S), ranges):
            return S.count('_')
        else:
            continue
    if S.count("_") ==len(S):
        return 0
    else:
        return S.count("_")


T = int(input())
for _ in range(T):
    N, Q = map(int, input().split())
    S = input()
    arr = list(map(int, input().split()))
    ranges = [list(map(int, input().split())) for i in range(Q)]

    out_ = goodString(N, Q, S, arr, ranges)
    print(out_)