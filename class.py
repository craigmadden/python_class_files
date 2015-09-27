class Rectangle(object):
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def get_area(self):
        return self.height * self.width

    def set_color(self, color_value):
        self.color_value = color_value

    def get_color(self):
        return self.color_value

m = Rectangle(50,50)

print m.get_area()

m.set_color('blue')

print m.get_color()