class Complex_number:

    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return Complex_number(self.real + other.real,
                              self.imag + other.imag)

    def __str__(self):
        return f"{self.real}+{self.imag}i"

num1 = Complex_number(3, 5)
num2 = Complex_number(4, 6)

result = num1 + num2

print(result)