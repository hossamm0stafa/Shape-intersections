from shapely.geometry import Polygon

# Define the polygons representing the boundaries of cities
city_boundaries = [
    Polygon([(0, 0), (0, 5), (5, 5), (5, 0)]),
    Polygon([(3, 2), (3, 7), (8, 7), (8, 2)]),
    Polygon([(10, 0), (10, 5), (15, 5), (15, 0)]),
    Polygon([(12, 2), (12, 7), (17, 7), (17, 2)]),
    Polygon([(20, 0), (20, 5), (25, 5), (25, 0)]),
    Polygon([(30, 10), (30, 15), (35, 15), (35, 10)]),
]

# Iterate through each pair of cities and find the intersection
for i in range(len(city_boundaries)):
    for j in range(i + 1, len(city_boundaries)):
        city1_boundary = city_boundaries[i]
        city2_boundary = city_boundaries[j]

        # Find the intersection
        intersection = city1_boundary.intersection(city2_boundary)

        # Check if there is an intersection
        if not intersection.is_empty:
            print(f"Intersection between Shape {i + 1} and Shape {j + 1}:", intersection.area)
        else:
            print(f"No intersection between Shape {i + 1} and Shape {j + 1}.")
