def split_arr(arr, n=4):
    div = len(arr)//n

    result = []
    start = 0
    end = div
    while end <= len(arr):
        if len(arr) - end < div and len(arr) - end > 0:
            end +=  len(arr) - end

        res = arr[start:end]
        start = end
        end += div
        result.append(res)
    return result


arr = list(map(int, input().split()))

[print(i) for i in split_arr(arr, n)]
