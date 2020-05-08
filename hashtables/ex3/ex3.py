def intersection(arrays):
    
    hash_arrays = { i: [0] for i in array[0]}

    n = len(arrays)

    result = []

    if n == 1:
        for i in hash_arrays:
            if len(hash_arrays[i]) == n:
                result.append(hash_arrays[i])
        
        return result
    
    for i in arrays[n]:
        if i in hash_arrays:
            hash_arrays[i].append[n]
        return intersection(arrays[n-1])

if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000,2000000)) + [1,2,3])
    arrays.append(list(range(2000000,3000000)) + [1,2,3])
    arrays.append(list(range(3000000,4000000)) + [1,2,3])

    print(intersection(arrays))
