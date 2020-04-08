def points_in_rectangle(points: list, rectangle_vertices: list, make_mockup_data=False) -> list:
    import random
    """
    :param points: list of (x,y) tuples for each point
    :param rectangle_edges: [(x,y), (x,y)] - bottom left and upper right corners
    :return: reduced list of points (which are within the boundary of the rectangle
    """

    if make_mockup_data:
        n = 100000
        m, dx, dy = (0, 0), 100, 100
        x, y = (m[0] - dx, m[0] + dx), (m[1] - dy, m[1] + dy)
        points = [(random.uniform(x[0], x[1]), random.uniform(y[0], y[1])) for i in range(n)]
        rectangle_vertices = [(random.uniform(x[0], x[1]), random.uniform(y[0], y[1])) for i in range(2)]

    dxr = max(rectangle_vertices[0][0], rectangle_vertices[1][0]) - min(rectangle_vertices[0][0], rectangle_vertices[1][0])
    dyr = max(rectangle_vertices[0][1], rectangle_vertices[1][1]) - min(rectangle_vertices[0][1], rectangle_vertices[1][1])

    print(f"rectangle area = {dxr*dyr}")

    return [point for point in points
            if (min(rectangle_vertices[0][0], rectangle_vertices[1][0]) <= point[0] <= max(rectangle_vertices[0][0], rectangle_vertices[1][0])) and
            (min(rectangle_vertices[0][1], rectangle_vertices[1][1]) <= point[1] <= max(rectangle_vertices[0][1], rectangle_vertices[1][1]))
            ]


if __name__ == "__main__":
    print(len(points_in_rectangle([], [], make_mockup_data=True)))
