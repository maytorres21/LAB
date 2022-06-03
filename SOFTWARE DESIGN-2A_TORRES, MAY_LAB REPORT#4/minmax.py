def min_max(S, index=0):
    if index == len(S) - 1:
        return S[index], S[index]
    else:
        min_c, max_c = min_max(S, index + 1)
        return min(S[index], min_c), max(S[index], max_c)


print(min_max([1, 2, 3, 4, 5, 6, 7, 8]))
print(min_max([-455, 2, 778, 5, 6, 7, 8]))
print(min_max([8, 7, 100, 5, 4, 3, 2, 1]))
