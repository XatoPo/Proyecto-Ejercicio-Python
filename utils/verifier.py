def count_sorted_prefix(arr):
    count = 1
    for i in range(1, len(arr)):
        if arr[i] >= arr[i - 1]:
            count += 1
        else:
            break
    return count