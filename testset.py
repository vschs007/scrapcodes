def calc_pending(ord, shifts):
    n = len(ord)
    res = []
    total_time = 0  # Track cumulative time to avoid array operations

    for shift in shifts:
        total_time += shift
        # Calculate how many complete sets of orders can be processed
        complete_sets = total_time // sum(ord)
        remaining_time = total_time % sum(ord)

        # Find number of pending orders
        processed = 0
        curr_time = remaining_time

        for i in range(n):
            if curr_time >= ord[i]:
                curr_time -= ord[i]
                processed += 1
            else:
                break

        pending = n - processed
        res.append(pending)

    return res
ord = [1, 2, 4, 1, 2]
shifts = [3, 10, 1, 1, 1]
result = print(calc_pending(ord, shifts))