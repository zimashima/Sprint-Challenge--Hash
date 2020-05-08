def has_negatives(a):

    hash_negatives = {}
    
    hash_negative = { i: (i*-1) for i in a if i < 0 }
    result = []
    for neg in hash_negative:
        result.append(hash_negative[neg])
    
    return result


if __name__ == "__main__":
    print(has_negatives([-1,-2,1,2,3,4,-4]))
