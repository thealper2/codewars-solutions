def peak_and_valley(arr):
    peaks_and_valleys = []
    n = len(arr)
    for i in range(n):
        is_peak = True
        is_valley = True
        for j in range(1, 4):
            if i - j >= 0:
                if arr[i] <= arr[i - j]:
                    is_peak = False
                if arr[i] >= arr[i - j]:
                    is_valley = False
            else:
                is_peak = False
                is_valley = False

        for j in range(1, 4):
            if i + j < n:
                if arr[i] <= arr[i + j]:
                    is_peak = False
                if arr[i] >= arr[i + j]:
                    is_valley = False
            else:
                is_peak = False
                is_valley = False
        if is_peak or is_valley:
            peaks_and_valleys.append(arr[i])
    return peaks_and_valleys
