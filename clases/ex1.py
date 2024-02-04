class StringProcessor:
    def __init__(self):
        self.input_string = ""

    def getString(self):
        self.input_string = input("Enter a string: ")

    def printString(self):
        print("String in uppercase:", self.input_string.upper())

# Test the class
if __name__ == "__main__":
    processor = StringProcessor()
    processor.getString()
    processor.printString()  
