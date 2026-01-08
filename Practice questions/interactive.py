low = 1
high = 10**6

while low < high:
    mid = (low + high + 1) // 2
    print(mid, flush=True)

    n = input()
    if n == ">=":
        low = mid
    else:
        high = mid - 1

print("! "+str(low), flush=True)