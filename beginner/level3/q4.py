class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length * self.length

if __name__ == "__main__":
    
    # square length - user input
    try:
        length = float(input("Enter length of the square:"))
        
        # Square instance with length from user input
        square = Square(length)
        print(f"Square area: {square.area()}")
        
    except ValueError:
        print("Enter a valid number for the length.")