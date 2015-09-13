a = 20   # the length of the first side
origin = (450/2.0,)*2
n = 1
w = TWO_PI / 120.0    # angular velocity of sweep
# Moving on to animate the next triangle is triggered
# by reaching a particular framecount, next_keyframe. 
last_keyframe = 0
next_keyframe = round(atan(1/sqrt(n))/w)
triangles = []

def setup():
    size(450, 450)
    background(0)
    frameRate(30)
    noFill()
    strokeWeight(2)
    stroke(255, 69, 0)

    
def draw():
    background(0)
    # Previously animated triangles are drawn anew
    for t in triangles:
        triangle(*t)
    phi = w * frameCount
    # The currently animated triangle's hypotenuse is calculated
    # such that the triangle is always right.
    theta = phi - (w * last_keyframe)
    x1, y1 = cart(sqrt(n)*a, w*last_keyframe, origin)
    x2, y2 = cart((sqrt(n)*a)/cos(theta), phi, origin)
    triangle(x1, y1, x2, y2, *origin)
    if frameCount == next_keyframe:
        # move on to animating the next triangle
        n += 1
        last_keyframe = next_keyframe
        next_keyframe += round(atan(1/sqrt(n))/w)
        t = (x1, y1, x2, y2, origin[0], origin[1])
        triangles.append(t)


def cart(r, theta, origin):
    '''Convert r and theta to cartesian coordinates with respect
       to origin.''' 
    x = origin[0] + (r * cos(theta))
    y = origin[1] - (r * sin(theta))
    return (x, y)
