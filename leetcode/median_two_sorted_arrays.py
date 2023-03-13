def findMedianSortedArrays(nums1, nums2) -> float:
    m = len(nums1)
    n = len(nums2)
    N = m + n
    med = N // 2  # index at where we can stop

    if m == n == 0:
        return 0
    elif m == 0:
        if N % 2 == 0:
            return (nums2[med - 1] + nums2[med]) / 2
        return nums2[med]
    elif n == 0:
        if N % 2 == 0:
            return (nums1[med - 1] + nums1[med]) / 2
        return nums1[med]

    i, j = 0, 0
    prev = 0
    curr = 0

    while i + j <= med:
        prev = curr
        if i == m:
            curr = nums2[j]
            j += 1
        elif j == n:
            curr = nums1[i]
            i += 1
        elif nums1[i] < nums2[j]:
            curr = nums1[i]
            i += 1
        else:
            curr = nums2[j]
            j += 1

    if N % 2 == 0:
        return (prev + curr) / 2
    else:
        return curr
