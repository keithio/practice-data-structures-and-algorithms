from math import sqrt


def find_closest_points(k, points):
    """
    Given 2D points, find k points that are closest to the origin.

    Time Complexity: O(n*k)
    Space Complexity: O(k)
    """
    if len(points) < k:
        return points

    k_points = [float('inf')] * k
    k_dists = [float('inf')] * k

    for point in points:
        # Calculate the distance for the point to the origin
        dist = sqrt(point[0] ** 2 + point[1] ** 2)

        # Find the current maximum distance of the k closets points
        max_k_dist = max(k_dists)

        # Get the index of the current maximum (note: only returns one index)
        max_k_index = k_dists.index(max_k_dist)

        # If the current point has a lesser distance, swap out the current
        # maximum point
        if dist < max_k_dist:
            k_dists[max_k_index] = dist
            k_points[max_k_index] = point

    return k_points
