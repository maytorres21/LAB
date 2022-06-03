def rec_find_max(S, index):
    if index == len(S) - 1:
        return S[index]
    return max(S[index], rec_find_max(S, index + 1))


def find_max(S):
    return rec_find_max(S, 0)


print(find_max([111, 2, 3, 4, 5, 6, 7, 8]))
print(find_max([1, 2, 7774, 5, 6, 7, 8]))
print(find_max([81, 7, 6, 119, 4, 3, 2, 1]))

