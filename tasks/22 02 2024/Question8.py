# show class method, static method and instance method with simple example. 


# Instance method

class MyClass:
    def __init__(self, x):
        self.x = x
    
    def instance_method(self):
        print("Instance method:")
        return self.x

obj = MyClass(5)
print(obj.instance_method())  # Calling instance method


# Class method

class MyClass:
    class_variable = 10

    def __init__(self, x):
        self.x = x
    
    @classmethod
    def class_method(cls):
        print("Class method :")
        return cls.class_variable

print(MyClass.class_method())  # Calling class method



# Static method

class MyClass:
    @staticmethod
    def static_method():
        print("Static method :")
        return "This is static method"

print(MyClass.static_method())  # Calling static method