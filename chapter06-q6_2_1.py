import math

class Cylinder:
    def __init__(self,radius,height):
        self.radius = radius
        self.height = height

    def volume(self):
        return math.pi * (self.radius ** 2) * self.height

    def surface_area(self):
        return 2 * math.pi * self.radius * (self.radius + self.height)

    def show_attributes(self):
        print(f"Radius: {self.radius}")
        print(f"Height: {self.height}")
        print(f"Volume: {self.volume():.2f}")
        print(f"Surface area: {self.surface_area():.2f}")

cylinder1 = Cylinder(radius=5, height=10)
cylinder1.show_attributes()
