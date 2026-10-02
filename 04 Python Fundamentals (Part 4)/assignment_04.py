import math

"""
=========================================================
Python Fundamentals - Assignment 4
=========================================================

Concept: Classes & Objects
---------------------------------------------------------
Q1. BankAccount
    - Attributes: account_number, owner_name, balance
    - Methods: deposit, withdraw, check_balance
"""
# print("-"*80)
# print("Bank Account Problem")
# print("-"*80)

# class BankAccount:
#     def __init__(self,account_number,owner_name,balance):
#         self.__account_number = account_number
#         self.__owner_name = owner_name
#         self.__balance = balance

#     def deposit(self, deposit_amount):
#         self.__balance += deposit_amount
#         print(f"You have successfully deposited {deposit_amount} into your account!!!")
#     def withdraw(self,withdrawl_amount):
#         if(self.__balance >= withdrawl_amount):
#             self.__balance -= withdrawl_amount
#             print(f"You have successfully withdrawn {withdrawl_amount} amount from your account!!!")
#         else:
#             print("You don't have the sufficient balance to withdraw!!!")

#     def check_balance(self):
#         print(f"Your current balance is: {self.__balance}")

# bank_acc1 = BankAccount(12345,"Nikesh",25100)
# bank_acc1.check_balance()
# bank_acc1.deposit(1000)
# bank_acc1.check_balance()
# bank_acc1.withdraw(20200)
# bank_acc1.check_balance()
# bank_acc1.withdraw(30000)
# bank_acc1.check_balance()
# print("-"*80)
"""
---------------------------------------------------------  
Q2. Book
    - Attributes: title, author, list of reviews
    - Methods: 
      * add a new review
      * count reviews
      * display all reviews
"""
# print("-"*80)
# print("Book Problem")
# print("-"*80)
# class Book:
#     def __init__(self,title,author,list_of_reviews=[]):
#         self.__title = title
#         self.__author = author
#         self.__list_of_reviews = list_of_reviews

#     def add_new_review(self):
#         new_review = input("Enter a new book review: ")
#         self.__list_of_reviews.append(new_review)
#         print("You have added the book review successfully!!!")

#     def count_reviews(self):
#         print(f"Review Count: {len(self.__list_of_reviews)}")

#     def display_reviews(self):
#         print("All the reviews: ")
#         if(len(self.__list_of_reviews)!=0):
#            for review in self.__list_of_reviews:
#             print(review)
#         else:
#            print("You don't have any reviews")

# book1 = Book("Book 1","Nikesh")
# book1.count_reviews()
# book1.display_reviews()
# book1.add_new_review()
# book1.count_reviews()
# book1.add_new_review()
# book1.add_new_review()
# book1.display_reviews()
# book1.count_reviews()

# print("-"*80)
"""
Concept: Encapsulation
---------------------------------------------------------
Q3. Student
    - Attributes: private _name, _roll_no, and _marks
    - Methods: Provide getter and setter methods with validation:
      * marks cannot be negative
      * roll number has to be between 1 & 100
      * name cannot be empty
"""
# print("-"*80)
# class Student:
#     def __init__(self,student_name,student_roll_no, student_marks):
#         if(student_name != " " or student_marks > 0 or (student_roll_no >= 1 and student_roll_no <= 100)):
#             self.__student_name = student_name
#             self.__student_roll_no = student_roll_no
#             self.__student_marks = student_marks
#         else:
#             print("You have incorrect argument. Please! check your arguments.")
#     def display_student_info(self):
#         print("Studnet Details: ")
#         print(f"Student Name: {self.__student_name}")
#         print(f"Student Roll No: {self.__student_roll_no}")
#         print(f"Student Marks: {self.__student_marks}")

#     def update_marks(self, new_marks):
#         self.__student_marks = new_marks
#         print("New marks is updated successfully!!!")

#     def update_roll(self,new_roll_no):
#         self.__student_roll_no = new_roll_no
#         print("New roll number is updated successfully!!!")


# print("-"*80)
# student1 = Student("Nikesh",24,95.5)
# student1.display_student_info()
# student1.update_marks(99.99)
# student1.update_roll(10)
# student1.display_student_info()
# print("-"*80)
"""
Concept: Function Overriding
---------------------------------------------------------
Q4. Shape
    - Create a base class Shape with a method area().
    - Create subclasses Circle, Rectangle, and Triangle that 
      override the area() method.
"""
# print("-"*80)
# print("Function Overriding: Shape Program")
# print("-"*80)
# class Shape:
#     def __init__(self,shape_name):
#         self._shape_name = shape_name

#     def area(self):
#         print("Print the area of the shape")


# class Circle(Shape):
#     def __init__(self,shape_name,radius):
#         super().__init__(shape_name)
#         self.__radius = radius

#     def area(self):
#         print(f"Area of the {self._shape_name} is: {(math.pi*self.__radius**2):.2f}")

# class Rectangle(Shape):
#     def __init__(self,shape_name,length,breadth):
#         super().__init__(shape_name)
#         self.__length = length
#         self.__breadth = breadth

#     def area(self):
#         print(f"Area of the {self._shape_name} is: {self.__length*self.__breadth}")

# class Triangle(Shape):
#     def __init__(self,shape_name,base,height):
#         super().__init__(shape_name)
#         self.__base = base
#         self.__height = height

#     def area(self):
#         print(f"Area of the {self._shape_name} is: {(0.5*self.__base*self.__height):.2f}")

# circle1 = Circle("Circle",7.08)
# circle1.area()

# rect1 = Rectangle("Rectangle",15,4)
# rect1.area()

# triangle1 = Triangle("Triangle",3,13)
# triangle1.area()
# print("-"*80)
"""
Concept: Inheritance
---------------------------------------------------------
Q5. Vehicle
    - Create a base class Vehicle with attributes like brand and model.
    - Create two subclasses, Car and Bike, that add extra attributes:
      * seats (in Car)
      * engine_cc (in Bike)

"""
# print("-"*80)
# print("Vehicle: Car, Bike Problem Question")
# class Vehicle:
#     def __init__(self,brand,model):
#         self._brand = brand
#         self._model = model

#     def vehicle_info(self):
#         pass

# class Bike(Vehicle):
#     def __init__(self,brand,model,engine_cc):
#         super().__init__(brand,model)
#         self.__engine_cc = engine_cc
#     def get_engine_cc(self):
#             return self.__engine_cc

# class Car(Vehicle):
#     def __init__(self,brand,model,seats):
#         super().__init__(brand,model)
#         self.__seats = seats

#     def get_seats(self):
#         return self.__seats

# print("-"*80)
# my_car = Car("Toyota", "Camry",5)
# my_bike = Bike("Yamaha", "R3", 21)

# print(f"Car: {my_car._brand} {my_car._model}, Seats: {my_car.get_seats()}")
# print(f"Bike: {my_bike._brand} {my_bike._model}, Engine: {my_bike.get_engine_cc()}cc")
# print("-"*80)

"""
Concept: Abstraction
---------------------------------------------------------
Q6. Employee
    - Create an abstract class Employee with an abstract method calculate_salary().
    - Create subclasses Intern, FullTimeEmployee, and ContractEmployee 
      that implement the method differently.
"""
# from abc import ABC, abstractmethod
# print("-"*80)
# print("Abstraction: Employee")
# class Employee(ABC):
#     def __init__(self,designation):
#         self._designation = designation

#     @abstractmethod
#     def calculate_salary(self):
#         pass
#     def get_designation(self):
#         return self._designation

# class Intern(Employee):
#     def __init__(self,designation,stipend):
#         super().__init__(designation)
#         self.__stipend = stipend

#     def calculate_salary(self):
#         print(f"Stipend of {self._designation} is: {self.__stipend}")

# class FullTimeEmployee(Employee):
#     def __init__(self,designation,monthly_salary):
#         super().__init__(designation)
#         self.__monthly_salary = monthly_salary

#     def calculate_salary(self):
#         print(f"Monthly Salary of {self._designation} is: {self.__monthly_salary}")

# class ContractEmployee(Employee):
#     def __init__(self,designation,hours_of_work,hourly_rate):
#         super().__init__(designation)
#         self.__hour_of_works = hours_of_work
#         self.__hourly_rate = hourly_rate

#     def calculate_salary(self):
#         print(f"Salary of {self._designation} is: {self.__hour_of_works* self.__hourly_rate}")
# print("-"*80)
# employees = [
#     Intern("Intern", 1000),
#     FullTimeEmployee("FullTimeEmployee", 5000),
#     ContractEmployee("ContractEmployee", 50, 80)
# ]

# for emp in employees:
#     emp.calculate_salary()
# print("-"*80)
"""
Concept: Constructor Overloading (with Default Parameters)
---------------------------------------------------------
Q7. Person
    - Create a class Person that allows the constructor to work with:
      * name only
      * name + age
      * name + age + address
    - Note: Use default parameters to simulate constructor overloading.
"""
# print("-"*80)
# print("Constructor Overloading with Default Parameters")
# class Person:
#     def __init__(self,name,age=None,address=None):
#         self.__name = name
#         self.__age = age
#         self.__address = address

#     def _get_name(self):
#         return self.__name

#     def _get_age(self):
#         return self.__age

#     def _get_address(self):
#         return self.__address

#     def display_details(self):
#         print(f"Name: {self._get_name()}")
#         print(f"Age: {self._get_age()}")
#         print(f"Address: {self._get_address()}")
# print("-"*80)
# # 1. Name only (uses default age and address)
# p1 = Person("Sita")
# p1.display_details()

# # 2. Name + Age (uses default address)
# p2 = Person("Ram", 20)
# p2.display_details()

# # 3. Name + Age + Address (provides all values)
# p3 = Person("Hari", 22, "Pokhara")
# p3.display_details()

"""
Concept: Instance & Class Attributes
---------------------------------------------------------
Q8. Player
    - Attributes: 
      * A class variable player_count
      * Instance variables name and level
    - Track how many players were created.
"""
# print("-" * 80)
# print("Instance and Class Attribute using Player Problem")


# class Player:
#     player_count = 0

#     def __init__(self, name, level):
#         self.__name = name
#         self.__level = level
#         Player.player_count += 1

#     def get_player_name(self):
#         return self.__name

#     def get_player_level(self):
#         return self.__level

#     @classmethod
#     def get_player_count(cls):
#         print(f"The current player count is: {Player.player_count}")


# print("-" * 80)
# Player.get_player_count()
# p1 = Player("Nikesh", "Intermediate")
# p2 = Player("Kaique", "Professional")
# p3 = Player("Nikhil", "Begineer")
# Player.get_player_count()

# print("-" * 80)
"""
Concept: Multiple Inheritance
---------------------------------------------------------
Q9. Bear
    - Create classes Herbivore, Carnivore, and Omnivore with some attributes & methods. 
    - Create a class Bear that inherits from all the above classes to showcase 
      how multiple inheritance works.
"""
# print("-" * 80)
# print("Multiple Inheritance: Bear Problem")
# print("-" * 80)


# # Base Class 1: Herbivore
# class Herbivore:

#     def __init__(self, plant_preference="Berries and Leaves"):
#         self.plant_preference = plant_preference

#     def graze(self):
#         return f"Grazing on plants: {self.plant_preference}"


# # Base Class 2: Carnivore
# class Carnivore:

#     def __init__(self, meat_preference="Fish and Meat"):
#         self.meat_preference = meat_preference

#     def hunt(self):
#         return f"Hunting for prey: {self.meat_preference}"


# # Base Class 3: Omnivore
# class Omnivore:

#     def __init__(self, foraging_skill="Expert"):
#         self.foraging_skill = foraging_skill

#     def forage(self):
#         return (
#             "Foraging across diverse habitats with"
#             f" {self.foraging_skill.lower()} skill."
#         )


# Derived Class: Bear inheriting from all three base classes
# class Bear(Carnivore, Herbivore, Omnivore):

#     def __init__(
#         self,
#         name,
#         plant_preference="Berries",
#         meat_preference="Salmon",
#         foraging_skill="Master",
#     ):
#         # Explicitly initialize all parent classes to avoid missing attributes
#         Herbivore.__init__(self, plant_preference)
#         Carnivore.__init__(self, meat_preference)
#         Omnivore.__init__(self, foraging_skill)
#         self.name = name

#     def display_behaviors(self):
#         return (
#             f"--- {self.name}'s Survival Skills ---\n"
#             f"1. {self.graze()}\n"
#             f"2. {self.hunt()}\n"
#             f"3. {self.forage()}"
#         )


# # --- Example Usage ---
# if __name__ == "__main__":
#   # Create an instance of Bear
# grizzly = Bear(
#     name="Grizzly",
#     plant_preference="Huckleberries",
#     meat_preference="Fresh Salmon",
#     foraging_skill="Master",
# )

# print(Bear.mro()[0])
# print(Bear.mro()[1])
# print(Bear.mro()[2])
# print(Bear.mro()[3])
#   # Access methods from all inherited parent classes
# print(grizzly.display_behaviors())

#   print("\n--- Method Resolution Order (MRO) ---")
#   # Python uses C3 Linearization to determine the order in which base classes are searched
#   for cls in Bear.__mro__:
#     print(cls.__name__)
# print("-" * 80)


