PHI = (1 + sqrt(5)) / 2

# spiral properties
a = 4
b = (2 * log(PHI)) / PI
c = (a / b) * sqrt(1 + b ** 2)
sep = 10    # separation of points along spiral
n = 300    # number of points


def setup():
    size(800, 500)
    background(241, 241, 241)
    frameRate(30)
    fill(255, 180, 2)
    noStroke()
    global origin
    origin = (24 * width / 34, 15 * height / 21)

    for i in xrange(n + 1):
        t = theta(i)
        r = a * exp(b*t)
        x, y = cart(r, t, origin)
        ellipse(x, y, 5, 5)


def draw():
    # sine wave properties
    k = TWO_PI / (7 * sep)
    w = TWO_PI / 120.0
    background(241, 241, 241)
    for i in xrange(n + 1):
        t = theta(i)
        sine_val = sin((k * c * (exp(b*t) - 1)) - (w * frameCount))
        amp_factor = (30 / exp(5*b*PI)) * exp(b*t)
        r = (a * exp(b*t)) + (amp_factor * sine_val)
        x, y = cart(r, t, origin)
        size = ((5 / exp(5*b*PI)) * exp(b*t)) + 3
        ellipse(x, y, size, size)


def cart(r, theta, origin):
    x = origin[0] + (r * cos(theta))
    y = origin[1] - (r * sin(theta))
    return (x, y)


def theta(n):
    t = 0
    while n > 0:
        t = (1.0 / b) * log((sep / c) + exp(b*t))
        n -= 1
    return t
