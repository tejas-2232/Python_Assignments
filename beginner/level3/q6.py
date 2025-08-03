# single inheritance
class Animal:
    def __init__(self,name):
        self.name = name
    
    def speak(self):
        return f"{self.name} makes a sound"
    

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
    
    def speak(self):
        return f"{self.name} is a {self.breed} and says woof"


# Multiple inheritance

class Printer:
    def print_document(self, document):
        return f"Printing document: {document}"

class Scanner:
    def scan_document(self):
        return "Scanning document......"

class MultiFunctionDevice(Printer, Scanner):
    def fax_document(self, document):
        return f"faxing document: {document}"


# mulitlevel inheritance

class Document:
    def __init__(self,title):
        self.title = title
    
    def info(self):
        return f"document title: {self.title}"

class FormattedDocument(Document):
    def __init__(self, title, style):
        super().__init__(title)
        self.style = style

    def info(self):
        return f"{super().info()} | Style: {self.style}"

class HTMLDocument(FormattedDocument):
    def __init__(self, title, style, charset):
        super().__init__(title, style)
        self.charset = charset

    def info(self):
        return f"{super().info()} | Charset: {self.charset}"



if __name__ == "__main__":
    # Single Inheritance 
    rex = Dog("Rex", "German Shepherd")
    print("Single Inheritance:")
    print(f"  {rex.speak()}")
    print(f"  Breed: {rex.breed}\n")

    # Multiple Inheritance 
    mfd = MultiFunctionDevice()
    print("Multiple Inheritance:")
    print(f"  {mfd.print_document('Hello')}")
    print(f"  {mfd.scan_document()}")
    print(f"  {mfd.fax_document('Hello')}\n")

    # Multilevel Inheritance
    html_doc = HTMLDocument("Report on AI", "Modern", "UTF-8")
    print("Multilevel Inheritance:")
    print(f"  {html_doc.info()}")