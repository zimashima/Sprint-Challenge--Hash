def get_indices_of_item_weights(weights, length, limit):

    hash_weight = {}

    for ind, i in enumerate(weights):
        if i in hash_weight:
            hash_weight[i].append(ind)
        else:
            hash_weight[i] = [ind]

    for i in hash_weight:
        diff = limit - i
        if (diff in hash_weight):
            if len(hash_weight[diff]) > 1:
                return [hash_weight[diff][1], hash_weight[diff][0]]
            else:
                return [hash_weight[diff][0], hash_weight[i][0]]
            
    return None
