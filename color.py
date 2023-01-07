def red(color):
    """Returns the red component of the color"""
    return color[0]

def green(color):
    """Returns the green component of the color"""
    return color[1]

def blue(color):
    """Returns the blue component of the color"""
    return color[2]

def color_distance(c1, c2):
    """Returns the distance between two colors"""
    r1 = red(c1)
    g1 = red(c1)
    b1 = red(c1)
    r2 = red(c2)
    g2 = red(c2)
    b2 = red(c2)

    return ((r1-r2)**2 + (g1-g2)**2 + (b1-b2)**2)**0.5
