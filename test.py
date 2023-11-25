from freegames import floor

def offset(point):
    """Return offset of point in tiles."""
    x = (floor(point[0], 20) + 200) / 20
    print(x)
    y = (180 - floor(point[1], 20)) / 20
    index = int(x + y * 20)
    return print(index)

offset((19,100))
