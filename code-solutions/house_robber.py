# O(n) , O(1)
def house_robber(house_values: list) -> int:
    if not house_values:
        return 0

    if len(house_values) == 1 :
        return house_values[0]
    
    previous, current = 0, 0

    for value in house_values:
        temp = max(previous + value, current)
        previous = current
        current = temp

    return current