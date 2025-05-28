# 1. Using self
# Assignment:
# Create a class Student with attributes name and marks. Use the self keyword to initialize these values via 
# a constructor. Add a method display() that prints student details.

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        return (f"Student Name: {self.name}, Marks: {self.marks}")
        
# Example usage
student1 = Student("Alice", 85)
print(student1.name)  # Output: Alice
print(student1.marks)  # Output: 85
print(student1.display())  # Output: Student Name: Alice, Marks: 85

# 2. Using cls
# Assignment:
# Create a class Counter that keeps track of how many objects  have been created. Use a class variable and a class\
# method with cls to manage and display the count.

class Counter:
    count = 5

    def __init__(self):
        Counter.count += 1

    @classmethod
    def display_count(cls):
        return f"Total objects created: {cls.count}"
    
# Create some objects
obj1 = Counter()
obj2 = Counter()
obj3 = Counter()

# Display the count using the class method
print(Counter.display_count()) # Output: Total objects created: 8

obj4 = Counter()
print(Counter.display_count()) # Output: Total objects created: 9

# 3. Public Variables and Methods
# Assignment:
# Create a class Car with a public variable brand and a public method start(). Instantiate the class and access 
# both from outside the class.

class Car:
    def __init__(self, brand):
        self.brand = brand  # Public variable

    def start(self):  # Public method
        return f"{self.brand} is starting."
    
# Example usage
car1 = Car("Toyota")
print(car1.brand)  # Output: Toyota
print(car1.start())  # Output: Toyota is starting.

# 4. Class Variables and Class Methods
# Assignment:
# Create a class Bank with a class variable bank_name. Add a class method change_bank_name(cls, name) that allows 
# changing the bank name. Show that it affects all instances.

class Bank:
    bank_name = "Global Bank"

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name
        
# Example usage
print(Bank.bank_name)  # Output: Global Bank
Bank.change_bank_name("Local Bank")  
print(Bank.bank_name)  # Output: Local Bank

# 5. Static Variables and Static Methods
# Assignment:
# Create a class MathUtils with a static method add(a, b) that returns the sum. No class or
# instance variables should be used.

class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b
    
# Example usage
print(MathUtils.add(5, 10))  # Output: 15

# 6. Constructors and Destructors
# Assignment:
# Create a class Logger that prints a message when an object is created (constructor) and another message when it 
# is destroyed (destructor).

class Logger:
    def __init__(self):
        print("Logger object created.")

    def __del__(self):
        print("Logger object destroyed.")

# Example usage
print("Creating Logger object...")
log1 = Logger()  # Output: Logger object created.
print("Deleting Logger object...")
del log1  # Output: Logger object destroyed.
print("Logger object is now deleted.")

# 7. Access Modifiers: Public, Private, and Protected
# Assignment:
# Create a class Employee with:

# a public variable name,

# a protected variable _salary, and

# a private variable __ssn.

# Try accessing all three variables from an object of the class and document what happens.

class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name      # Public variable
        self._salary = salary   # Protected variable
        self.__ssn = ssn       # Private variable

emp1 = Employee("John Doe", 50000, "123-45-6789")
print(emp1.name)          # Output: John Doe (Public access)
print(emp1._salary)       # Output: 50000 (Protected access, but still accessible)
# print(emp1.__ssn)# Raises AttributeError: 'Employee' object has no attribute '__ssn' but can be accessed using _Employee__ssn(name mangling)
print(emp1._Employee__ssn)  # Output: 123-45-6789 (Accessing private variable using name mangling)

# 8. The super() Function
# Assignment:
# Create a class Person with a constructor that sets the name. Inherit a class Teacher from it,add a subject field, and use 
# super() to call the base class constructor.

class person:
    def __init__(self, name):
        self.name = name
        
class Teacher(person):
    def __init__(self, name, subject):
       super().__init__(name)
       self.subject = subject
    
# Example Usage:
teacher1 = Teacher("Mr. Jones", "Physics")
print(f"Teacher Name: {teacher1.name}")
print(f"Teacher Subject: {teacher1.subject}")

# 9. Abstract Classes and Methods
# Assignment:
# Use the abc module to create an abstract class Shape with an abstract method area(). 
# Inherit a class Rectangle that implements area().

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
     pass
        
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    
# Example usage
rect1 = Rectangle(5, 10)
print(f"Area of Rectangle: {rect1.area()}")  # Output: Area of Rectangle: 50

# 10. Instance Methods
# Assignment:
# Create a class Dog with instance variables name and breed. Add an instance method bark()
# that prints a message including the dog's name.

class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    
    def bark(self):
        print(f"{self.name} says Woof! I am a {self.breed}.")
        
# Example usage
dog1 = Dog("Buddy", "Golden Retriever")
print(dog1.name)  # Output: Buddy
print(dog1.breed)  # Output: Golden Retriever
dog1.bark()  # Output: Buddy says Woof! I am a Golden Retriever.

# 11. Class Methods
# Assignment:
# Create a class Book with a class variable total_books. Add a class method increment_book_count() to increase
# the count when a new book is added.

class Book:
    total_books = 0

    def __init__(self, title): # Only expects title
        self.title = title
        Book.increment_book_count()

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1

# Example usage (adjusted to pass only title)
print(f"Initial total books: {Book.total_books}")

book1 = Book("The Hitchhiker's Guide to the Galaxy") # Only pass title
print(f"After adding '{book1.title}': {Book.total_books} books")

book2 = Book("Pride and Prejudice") # Only pass title
print(f"After adding '{book2.title}': {Book.total_books} books")

book3 = Book("1984") # Only pass title
print(f"After adding '{book3.title}': {Book.total_books} books")

print(f"\nFinal total books: {Book.total_books}")

# 12. Static Methods
# Assignment:
# Create a class TemperatureConverter with a static method celsius_to_fahrenheit(c) that returns the Fahrenheit value.

class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        """
        Converts a temperature from Celsius to Fahrenheit.
        Formula: F = (C * 9/5) + 32
        """
        return (celsius * 9/5) + 32

# --- Example Usage ---

# Convert 0 degrees Celsius
celsius1 = 0
fahrenheit1 = TemperatureConverter.celsius_to_fahrenheit(celsius1)
print(f"{celsius1}°C is {fahrenheit1}°F") # Expected: 32.0°F

# Convert 25 degrees Celsius
celsius2 = 25
fahrenheit2 = TemperatureConverter.celsius_to_fahrenheit(celsius2)
print(f"{celsius2}°C is {fahrenheit2}°F") # Expected: 77.0°F

# Convert -10 degrees Celsius
celsius3 = -10
fahrenheit3 = TemperatureConverter.celsius_to_fahrenheit(celsius3)
print(f"{celsius3}°C is {fahrenheit3}°F") # Expected: 14.0°F

# Convert 100 degrees Celsius (boiling point)
celsius4 = 100
fahrenheit4 = TemperatureConverter.celsius_to_fahrenheit(celsius4)
print(f"{celsius4}°C is {fahrenheit4}°F") # Expected: 212.0°F

# # 13. Composition
# Assignment:
# Create a class Engine and a class Car. Use composition by passing an Engine object to the Car class during initialization. Access a 
# method of the Engine class via the Car class.

class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

    def start(self):
        """
        Simulates starting the engine.
        """
        return f"Engine with {self.horsepower} HP is starting..."

class Car:
    def __init__(self, make, model, engine_object):
        self.make = make
        self.model = model
        self.engine = engine_object  # Composition: Car "has a" Engine

    def drive(self):
        """
        Simulates driving the car, which involves starting its engine.
        """
        print(f"The {self.make} {self.model} is ready to drive.")
        # Accessing Engine's method through the Car object
        print(self.engine.start())
        return f"The {self.make} {self.model} is driving!"

# --- Example Usage ---

# 1. Create an Engine object
my_engine = Engine(horsepower=300)

# 2. Create a Car object, passing the Engine object to it
my_car = Car(make="Toyota", model="Camry", engine_object=my_engine)

# 3. Access a method of the Engine class via the Car class
print(my_car.drive())

print("\n--- Another Car ---")
sports_engine = Engine(horsepower=500)
sports_car = Car(make="Ferrari", model="F8", engine_object=sports_engine)
print(sports_car.drive())

# 14. Aggregation
# Assignment:
# Create a class Department and a class Employee. Use aggregation by having a Department object store a reference
# to an Employee object that exists independently of it.

class Employee:
    def __init__(self, employee_id, name):
        self.employee_id = employee_id
        self.name = name

    def get_details(self):
        """
        Returns a string with the employee's ID and name.
        """
        return f"Employee ID: {self.employee_id}, Name: {self.name}"

class Department:
    def __init__(self, name, head=None):
        self.name = name
        # Aggregation: The Department stores a reference to an Employee object.
        # The Employee object can exist without the Department.
        self.head = head

    def display_department_info(self):
        """
        Displays the department's name and its head's details.
        """
        info = f"Department: {self.name}"
        if self.head:
            info += f"\nDepartment Head: {self.head.get_details()}"
        else:
            info += "\nDepartment Head: Not assigned"
        return info

# --- Example Usage ---

# 1. Create Employee objects independently
employee1 = Employee(101, "Alice Smith")
employee2 = Employee(102, "Bob Johnson")
employee3 = Employee(103, "Charlie Brown")

print("--- Employee Objects Created ---")
print(employee1.get_details())
print(employee2.get_details())
print(employee3.get_details()) # This employee is not assigned to a department head role yet

print("\n--- Departments Created ---")

# 2. Create Department objects, assigning existing Employee objects as heads
hr_department = Department("Human Resources", head=employee1)
it_department = Department("Information Technology", head=employee2)
finance_department = Department("Finance") # Department without an assigned head initially

# 3. Display department information
print(hr_department.display_department_info())
print("-" * 30)
print(it_department.display_department_info())
print("-" * 30)
print(finance_department.display_department_info())

print("\n--- Assigning a Head to Finance Department ---")
# 4. We can assign an existing employee later
finance_department.head = employee3
print(finance_department.display_department_info())

# Important Note: If 'employee1' was deleted, 'hr_department' would still exist,
# but its 'head' reference would become invalid or 'None' if handled explicitly.
# The 'employee1' object itself doesn't depend on 'hr_department' for its existence.

# 15. Method Resolution Order (MRO) and Diamond Inheritance
# Assignment:
# Create four classes:

# A with a method show(),

# B and C that inherit from A and override show(),

# D that inherits from both B and C.

# Create an object of D and call show() to observe MRO.

class A:
    def show(self):
        return "Method from Class A"
        
        
class B(A):
    def show(self):
        return "Method from Class B"
    
class C(A):
    def show(self):
        return "Method from Class C"
    
class D(B, C):
    pass

# Create an object of D
d_obj = D()

# Call show() to observe MRO
d_obj.show()

# Print the MRO of class D
print(D.__mro__)

# 16. Function Decorators
# Assignment:
# Write a decorator function log_function_call that prints "Function is being called" before a
# function executes. Apply it to a function say_hello().

def log_function_call(func):
    """
    A decorator that prints 'Function is being called' before
    the decorated function executes.
    """
    def wrapper(*args, **kwargs):
        print("Function is being called")
        return func(*args, **kwargs)
    return wrapper

@log_function_call
def say_hello():
    """
    A simple function that prints a greeting.
    """
    print("Hello, world!")

# Call the decorated function
say_hello()

# 17. Class Decorators
# Assignment:
# Create a class decorator add_greeting that modifies a class to add a greet() method 
# returning "Hello from Decorator!". Apply it to a class Person.

def add_greeting(cls):
    """
    A class decorator that adds a 'greet' method to the decorated class.
    The 'greet' method returns "Hello from Decorator!".
    """
    def greet(self):
        return "Hello from Decorator!"

    # Add the 'greet' method to the class
    setattr(cls, 'greet', greet)

    return cls

@add_greeting
class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        return f"My name is {self.name}."

# Create an instance of the decorated Person class
person_obj = Person("Alice")

# Call the original method
print(person_obj.introduce())

# Call the method added by the decorator
print(person_obj.greet())

# 18. Property Decorators: @property, @setter, and @deleter
# Assignment:
# Create a class Product with a private attribute _price. Use @property to get the price,
# @price.setter to update it, and @price.deleter to delete it.
    
class Product:
    def __init__(self, initial_price):
        # This is our actual storage for the price.
        # The underscore `_` means "don't touch this directly from outside".
        self._price = None
        # We use our setter to set the initial price safely
        self.price = initial_price

    @property
    def price(self):
        """
        GETTER: When you ask for `product.price`.
        """
        print("Someone is getting the price!")
        return self._price

    @price.setter
    def price(self, new_price):
        """
        SETTER: When you say `product.price = some_value`.
        """
        if not isinstance(new_price, (int, float)):
            raise ValueError("Price must be a number!")
        if new_price < 0:
            raise ValueError("Price cannot be negative!")
        print(f"Someone is setting the price to {new_price}!")
        self._price = new_price

    @price.deleter
    def price(self):
        """
        DELETER: When you say `del product.price`.
        """
        print("Someone is deleting the price!")
        del self._price
        print("Price has been removed.")

# --- Let's see it in action! ---

# 1. Create a product
my_product = Product(50) # This uses the @price.setter behind the scenes

# 2. Get the price
print(f"The current price is: {my_product.price}") # This uses the @property getter

# 3. Change the price
my_product.price = 75 # This uses the @price.setter again
print(f"The new price is: {my_product.price}")

# 4. Try to set a bad price (it will stop us!)
try:
    my_product.price = -10
except ValueError as e:
    print(f"Error: {e}")

# 5. Delete the price
del my_product.price # This uses the @price.deleter

# 6. Try to get the price after deleting it (it will fail)
try:
    print(my_product.price)
except AttributeError as e:
    print(f"Error: {e}")
    
# 19. callable() and __call__()
# Assignment:
# Create a class Multiplier with an __init__() to set a factor. Define a __call__() method that multiplies an input 
# by the factor. Test it with callable() and by calling the object like a function.

class Multiplier:
    def __init__(self, factor):
        """
        Initializes the Multiplier object with a given factor.
        """
        if not isinstance(factor, (int, float)):
            raise TypeError("Factor must be a number (int or float).")
        self.factor = factor
        print(f"Multiplier created with factor: {self.factor}")

    def __call__(self, value):
        """
        Makes instances of Multiplier callable like functions.
        When called, it multiplies the input 'value' by the stored factor.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("Input value must be a number (int or float).")
        print(f"__call__ method invoked: {value} * {self.factor}")
        return value * self.factor

# --- Testing the Multiplier class ---

print("--- Creating Multiplier Objects ---")
# Create an instance of Multiplier with a factor of 5
multiply_by_5 = Multiplier(5)

# Create another instance with a factor of 2.5
multiply_by_2_5 = Multiplier(2.5)

# --- Testing callable() ---
print("\n--- Testing callable() ---")
print(f"Is 'multiply_by_5' callable? {callable(multiply_by_5)}")
print(f"Is 'multiply_by_2_5' callable? {callable(multiply_by_2_5)}")
print(f"Is the class 'Multiplier' callable? {callable(Multiplier)}") # Classes are callable (to create instances)
print(f"Is a regular integer (5) callable? {callable(5)}") # Integers are not callable
print(f"Is a string ('hello') callable? {callable('hello')}") # Strings are not callable

# --- Testing by calling the object like a function ---
print("\n--- Calling Objects Like Functions ---")

result1 = multiply_by_5(10) # Calls multiply_by_5.__call__(10)
print(f"10 multiplied by 5: {result1}")

result2 = multiply_by_2_5(8) # Calls multiply_by_2_5.__call__(8)
print(f"8 multiplied by 2.5: {result2}")

result3 = multiply_by_5(3.5) # Calls multiply_by_5.__call__(3.5)
print(f"3.5 multiplied by 5: {result3}")

# --- Example of invalid input ---
print("\n--- Testing with Invalid Input ---")
try:
    multiply_by_5("hello")
except TypeError as e:
    print(f"Error: {e}")

try:
    Multiplier("factor") # Invalid factor during initialization
except TypeError as e:
    print(f"Error: {e}")
    
# 20. Creating a Custom Exception
# Assignment:
# Create a custom exception InvalidAgeError. Write a function check_age(age) that raises this 
# exception if age < 18. Handle it with try...except.

class InvalidAgeError(Exception):
    """
    Custom exception raised when an invalid age is provided.
    """
    def __init__(self, age, message="Age must be 18 or older."):
        self.age = age
        self.message = f"Invalid age: {age}. {message}"
        super().__init__(self.message) # Call the base class constructor
        
def check_age(age):
    """
    Checks if the given age is 18 or older.
    Raises InvalidAgeError if age is less than 18.
    """
    if not isinstance(age, (int, float)):
        raise TypeError("Age must be a number.")
    if age < 0:
        raise ValueError("Age cannot be negative.")

    if age < 18:
        raise InvalidAgeError(age) # Raise our custom exception
    else:
        print(f"Age {age} is valid. Welcome!")
        
# --- Testing with try...except ---

print("--- Testing Age Validity ---")

# Valid age
try:
    check_age(20)
except InvalidAgeError as e:
    print(f"Caught an error: {e}")
except (TypeError, ValueError) as e:
    print(f"Caught a general error: {e}")
print("-" * 30)

# Invalid age (less than 18)
try:
    check_age(16)
except InvalidAgeError as e:
    print(f"Caught an InvalidAgeError: {e}")
except (TypeError, ValueError) as e:
    print(f"Caught a general error: {e}")
print("-" * 30)

# Invalid age (negative) - Caught by ValueError
try:
    check_age(-5)
except InvalidAgeError as e:
    print(f"Caught an InvalidAgeError: {e}")
except (TypeError, ValueError) as e:
    print(f"Caught a general error: {e}")
print("-" * 30)

# Invalid age (wrong type) - Caught by TypeError
try:
    check_age("twenty")
except InvalidAgeError as e:
    print(f"Caught an InvalidAgeError: {e}")
except (TypeError, ValueError) as e:
    print(f"Caught a general error: {e}")
print("-" * 30)

# 21. Make a Custom Class Iterable
# Assignment:
# Create a class Countdown that takes a start number. Implement __iter__() and __next__() to make the object
# iterable in a for-loop, counting down to 0.

class Countdown:
    def __init__(self, start_number):
        # Ensure the starting number is a non-negative integer.
        if not isinstance(start_number, int) or start_number < 0:
            raise ValueError("Start number must be a non-negative integer.")
        self.start_number = start_number
        self.current_number = start_number

    def __iter__(self):
        # Reset the current number to the start, allowing re-iteration.
        self.current_number = self.start_number
        return self # The object itself is the iterator.

    def __next__(self):
        # If there are numbers left, return the current one and decrement.
        if self.current_number >= 0:
            value = self.current_number
            self.current_number -= 1
            return value
        # If no numbers are left, signal the end of iteration.
        else:
            raise StopIteration
        
# Create a Countdown object that starts from 3
my_countdown = Countdown(3)

# Iterate through the countdown and print each number
print("Counting down:")
for num in my_countdown:
    print(num)

# Expected output:
# Counting down:
# 3
# 2
# 1
# 0