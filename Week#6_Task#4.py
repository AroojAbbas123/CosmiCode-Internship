import collections
from collections import defaultdict, Counter, namedtuple

# Using namedtuple for complex number history tracking
ComplexOperation = namedtuple('ComplexOperation', ['operation', 'operand1', 'operand2', 'result'])

class Complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self._operation_history = collections.deque(maxlen=10)  # Track last 10 operations
        
    def display(self):
        if self.b >= 0:
            print(f"The complex number is {self.a} + {self.b}i")
        else:
            print(f"The complex number is {self.a} - {-self.b}i")
   
    def add(self, other):
        real_part = self.a + other.a
        imaginary_part = self.b + other.b
        result = Complex(real_part, imaginary_part)
        self._record_operation('add', self, other, result)
        return result
    
    def subtract(self, other):
        real_part = self.a - other.a
        imaginary_part = self.b - other.b
        result = Complex(real_part, imaginary_part)
        self._record_operation('subtract', self, other, result)
        return result
    
    def multiply(self, other):
        real_part = self.a * other.a - self.b * other.b
        imaginary_part = self.a * other.b + self.b * other.a
        result = Complex(real_part, imaginary_part)
        self._record_operation('multiply', self, other, result)
        return result
    
    def divide(self, other):
        denominator = other.a**2 + other.b**2
        if denominator == 0:
            raise ValueError("Cannot divide by zero.")
        real_part = (self.a * other.a + self.b * other.b) / denominator
        imaginary_part = (self.b * other.a - self.a * other.b) / denominator
        result = Complex(real_part, imaginary_part)
        self._record_operation('divide', self, other, result)
        return result
    
    def equal(self, other):
        return self.a == other.a and self.b == other.b
    
    def notEqual(self, other):
        return not self.equal(other)
    
    def _record_operation(self, operation, operand1, operand2, result):
        """Record operations using deque to maintain history"""
        self._operation_history.append(
            ComplexOperation(operation, operand1, operand2, result))
    
    def get_operation_history(self):
        """Return operation history as a list"""
        return list(self._operation_history)
    
    def get_operation_stats(self):
        """Return operation statistics using Counter"""
        return Counter(op.operation for op in self._operation_history)

def analyze_complex_numbers(complex_numbers):
    """Analyze a collection of complex numbers using defaultdict"""
    analysis = defaultdict(list)
    for c in complex_numbers:
        magnitude = (c.a**2 + c.b**2)**0.5
        analysis['magnitudes'].append(magnitude)
        analysis['real_parts'].append(c.a)
        analysis['imaginary_parts'].append(c.b)
    return analysis

def main():
    # Input using defaultdict to handle missing values
    inputs = defaultdict(int)
    prompts = [
        "real part of the first complex number",
        "imaginary part of the first complex number",
        "real part of the second complex number",
        "imaginary part of the second complex number"
    ]
    
    for i, prompt in enumerate(prompts):
        while True:
            try:
                inputs[i] = int(input(f"Enter the {prompt}: "))
                break
            except ValueError:
                print("Please enter a valid integer.")

    c1 = Complex(inputs[0], inputs[1])
    c2 = Complex(inputs[2], inputs[3])

    print("\nDetails of the complex numbers:")
    c1.display()
    c2.display()

    # Perform operations
    operations = [
        ("Addition", c1.add(c2)),
        ("Subtraction", c1.subtract(c2)),
        ("Multiplication", c1.multiply(c2)),
        ("Division", c1.divide(c2))
    ]

    for name, op in operations:
        print(f"\n{name} of the two complex numbers:")
        op.display()

    # Equality check
    print("\nChecking if the two complex numbers are equal:")
    print("Equal" if c1.equal(c2) else "Not equal")

    # Operation history analysis
    print("\nOperation History Analysis:")
    print(f"First complex number operations: {c1.get_operation_stats()}")
    print(f"Second complex number operations: {c2.get_operation_stats()}")

    # Collection analysis
    complex_numbers = [c1, c2, operations[0][1], operations[1][1], operations[2][1], operations[3][1]]
    analysis = analyze_complex_numbers(complex_numbers)
    print("\nStatistical Analysis of all generated complex numbers:")
    print(f"Real parts: {analysis['real_parts']}")
    print(f"Imaginary parts: {analysis['imaginary_parts']}")
    print(f"Magnitudes: {[round(m, 2) for m in analysis['magnitudes']]}")

if __name__ == "__main__":
    
    main()