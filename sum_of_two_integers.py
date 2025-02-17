def sum_of_two_integers(a:int, b:int)-> int:
    MASK= 0xFFFFFFFF
    MASK_MAX_INT = 0x7FFFFFFF
    
    while b!=0 & MASK:
        carry = a & b
        a = (a ^ b )& MASK
        b = (carry << 1) & MASK
    
    if a <= MASK_MAX_INT:
        return a
    else:
        return a - (MASK +1)
        
        