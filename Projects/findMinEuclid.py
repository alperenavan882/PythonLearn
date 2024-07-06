import math

# 1. Define points
points = [(1, 2), (4, 6), (7, 8), (2, 1), (5, 3)]

# 2. Type a func for Euclid distance
def euclideanDistance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# 3. Calculate distances
distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        dist = euclideanDistance(points[i], points[j])
        distances.append(dist)

# 4. Find minimum distance and print
min_distance = min(distances)
print("Min distance = ", min_distance)
