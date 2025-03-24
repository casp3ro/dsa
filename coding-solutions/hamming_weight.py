def hamming_weight(n:int)-> int:
    output = 0
    
    while n:
        output += n & 1
        n = n >> 1
    
    return output