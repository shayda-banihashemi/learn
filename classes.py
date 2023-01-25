class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print('hello', self.name, self.age)

employee = Person('Andy', 18)
print(type(employee))
employee.say_hello()

manager = Person('Sam', 21)
manager.say_hello()