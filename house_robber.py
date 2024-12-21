# O(n) , O(1)
def house_robber(house_values: list) -> int:
    previous, current = 0, 0

    for value in house_values:
        previous, current = current, max(previous + value, current)

    return current