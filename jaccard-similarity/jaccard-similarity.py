def jaccard_similarity(set_a, set_b):
    """
    Compute the Jaccard similarity between two item sets.
    """
    # Write code here
    a = set(set_a)
    b = set(set_b)
    
    # If both sets are empty
    if len(a) == 0 and len(b) == 0:
        return 0.0
    
    intersection = a.intersection(b)
    union = a.union(b)
    
    return len(intersection) / len(union)