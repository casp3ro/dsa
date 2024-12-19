# O(n) time O(1) space

def climb_stairs(n: int) -> int:
    if n <= 1:
        return 1
    
    p1, p2 = 1, 1
    
    for _ in range(n - 1):
        p1, p2 = p1 + p2, p1
    
    return p1