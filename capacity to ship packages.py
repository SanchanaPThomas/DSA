def shipWithinDays(weights, days):
    left = max(weights)
    right = sum(weights)

    def canShip(capacity):
        curr_weight = 0
        needed_days = 1

        for w in weights:
            if curr_weight + w > capacity:
                needed_days += 1
                curr_weight = 0
            curr_weight += w

        return needed_days <= days

    while left < right:
        mid = (left + right) // 2

        if canShip(mid):
            right = mid
        else:
            left = mid + 1

    return left
