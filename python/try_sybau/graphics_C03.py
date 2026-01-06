graphics/
│
├── rectangle.py
├── circle.py
│
└── graphics3d/
    ├── cuboid.py
    └── sphere.py


#graphics/rectangle.py
def area(l, b):
    return l * b

def perimeter(l, b):
    return 2 * (l + b)

# graphics/circle.py
def area(r):
    return 3.14 * r * r

def perimeter(r):
    return 2 * 3.14 * r

# graphics/graphics3d/cuboid.py
def area(l, b, h):
    return 2 * (l*b + b*h + l*h)

def perimeter(l, b, h):
    return 4 * (l + b + h)

# graphics/graphics3d/sphere.py
def area(r):
    return 4 * 3.14 * r * r

def perimeter(r):
    return 2 * 3.14 * r

# Selective import
from graphics.rectangle import area, perimeter

print("Rectangle Area:", area(4, 5))
print("Rectangle Perimeter:", perimeter(4, 5))

# Import module
import graphics.circle as c

print("Circle Area:", c.area(3))
print("Circle Perimeter:", c.perimeter(3))

# Import from sub-package
from graphics.graphics3d.cuboid import area, perimeter

print("Cuboid Area:", area(2, 3, 4))
print("Cuboid Perimeter:", perimeter(2, 3, 4))

# import *
from graphics.graphics3d.sphere import *

print("Sphere Area:", area(5))
print("Sphere Perimeter:", perimeter(5))

