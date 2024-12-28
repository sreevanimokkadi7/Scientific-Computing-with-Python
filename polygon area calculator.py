class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"
        
    def set_width(self, width):
        self.width = width
    
    def set_height(self, height):
        self.height=height
    
    def get_area(self):
        return self.width * self.height
    
    def get_perimeter(self):
        return (2 * self.width) + (2 * self.height)

    def get_diagonal(self):
        return ((self.width ** 2 + self.height ** 2 ) ** .5)
    
    def get_picture(self):
        '''Returns a string that represents the shape using lines of "*". The number of lines equal to the height and the number of "*" in each line should be equal to the width. There should be a new line (\n) at the end of each line. If the width or height is larger than 50, this should return the string: "Too big for picture.".'''
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        
        s = ''
        for row in range(self.height):
            s += "*" * self.width + "\n"
        return s
        
    def get_amount_inside(self, shape):
        '''Takes another shape (square or rectangle) as an argument. Returns the number of times the passed in shape could fit inside the shape (with no rotations). For instance, a rectangle with a width of 4 and a height of 8 could fit in two squares with sides of 4.'''
        s_area = shape.get_area()
        l_area = self.get_area()
        return l_area // s_area

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
    
    def __str__(self):
        return f"Square(side={self.height})"
    
    def set_side(self, side):
        self.width = side
        self.height = side
    
    def set_width(self, side):
        self.set_side(side)

    def set_height(self, side):
        self.set_side(side)
