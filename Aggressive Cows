
# Aggressive Cows
def aggressiveCows(stalls, k):
    stalls.sort()
    def canPlaceCows(distance):
        count, last_position = 1, stalls[0]
        for stall in stalls[1:]:
            if stall - last_position >= distance:
                count += 1
                last_position = stall
            if count == k:
                return True
        return False
    low, high = 1, stalls[-1] - stalls[0]
    while low <= high:
        mid = (low + high) // 2
        if canPlaceCows(mid):
            low = mid + 1
        else:
            high = mid - 1
    return high
