from math import sqrt


def find_k_closest_points(k, points):
    """
    Given 2D points, find k points that are closest to the origin.

    Should run in O(n*k)
    """
    if len(points) < k:
        return points

    k_closest_points = [float('inf')] * k
    k_closest_dists = [float('inf')] * k

    for point in points:
        dist = sqrt(point[0] ** 2 + point[1] ** 2)
        for i in range(k):
            if dist < k_closest_dists[i]:
                k_closest_dists[i] = dist
                k_closest_points[i] = point
                break

    return k_closest_points


if __name__ == '__main__':
    from random import uniform
    points = [(uniform(0, 20), uniform(0, 20)) for i in range(20)]
    print points
    print ""
    print find_k_closest_points(5, points)
