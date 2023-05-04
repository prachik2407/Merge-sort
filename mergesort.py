def mergesort(array):
    if len(array)<2:
        return array

    mid = len(array) // 2
    left = mergesort(array[:mid])
    right = mergesort(array[mid:])
    return merge(left, right)



def merge(left, right):
    result =[]
    i, j = 0, 0
    while i<len(left) or j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
        if i == len(left) or j == len(right):
            result.extend(left[i:] or right[j:])
            break
    return result

a = [55,25,48,14,22,224]
print(mergesort(a))