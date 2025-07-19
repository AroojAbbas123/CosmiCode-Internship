class FileHandler:
    def __init__(self, filename):
        """Initialize with a filename"""
        self.filename = filename
    
    def read(self):
        """Read entire file content"""
        try:
            with open(self.filename, 'r') as file:
                return file.read()
        except FileNotFoundError:
            return "File not found"
        except IOError:
            return "Error reading file"
    
    def write(self, content):
        """Overwrite file with new content"""
        try:
            with open(self.filename, 'w') as file:
                file.write(content)
            return True
        except IOError:
            return False
    
    def append(self, content):
        """Add content to end of file"""
        try:
            with open(self.filename, 'a') as file:
                file.write(content)
            return True
        except IOError:
            return False
    
    def clear(self):
        """Empty the file"""
        return self.write("")
    
    def read_lines(self):
        """Read file as list of lines"""
        try:
            with open(self.filename, 'r') as file:
                return file.readlines()
        except FileNotFoundError:
            return []
    
    def __str__(self):
        return f"FileHandler for '{self.filename}'"

def main():
    file = FileHandler("example.txt")
    
    file.write("Hello World!\n")
    
    file.append("This is line 2\n")
    
    print("Full content:")
    print(file.read())
    
    print("\nAs lines:")
    for line in file.read_lines():
        print(line.strip())
    
    file.clear()
    print("\nAfter clearing:", file.read())
    
    
if __name__ == "__main__":
    main()