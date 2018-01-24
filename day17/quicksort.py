def qsort(items):
    if len(items) <= 1:
        return items
    if len(items) < 3:
        if items[0] > items[1]:
            return [items[1], items[0]]

    pivot = items[0]
    left = []
    right = []

    for item in items[1:]:
        if item < pivot:
            left.append(item)
        else:
            right.append(item)

    return qsort(left) + [pivot] + qsort(right)
