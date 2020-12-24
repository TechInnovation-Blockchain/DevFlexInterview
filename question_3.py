def solve(target, points, cur, solved):
    # write your code here
    if points[cur] == target:
        return solved + 1
    elif points[cur] > target:
        return len(points)
    
    tmp1 = len(points)
    tmp2 = len(points)
    if len(points) > cur + 2:
        tmp1 = solve(target, points, cur + 2, solved + 1)
    if len(points) > cur + 1:
        tmp2 = solve(target, points, cur + 1, solved + 1)
    
    return min(tmp1, tmp2)

def minimum_points(threshold, points):
    return solve(points[0] + threshold, points, 0, 0)

if __name__ == "__main__":
    # write your debug code here
    pass