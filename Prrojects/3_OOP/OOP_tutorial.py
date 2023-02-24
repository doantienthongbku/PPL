class Employee:
    """common base class for all employees"""
    empCount = 0                        # static field
    def __init__(self, name, salary):   # constructor
        self.name = name                # instance field
        self.salary = salary            # instance field
        Employee.empCount += 1
    
    def displayEmployee(self):          # instance method
        print("Name: ", self.name, ", Salary: ", self.salary)
        
    @classmethod                        # class method
    def create(cls, name, salary):
        print(cls.empCount)
        return cls(name, salary)
    
    @staticmethod                       # static method
    def isHighSal(salary):
        if (salary > 18):
            print("High salary")
            
    """Encapsulation in python
        - Public: begin with a letter
        - Protected: begin with a single underscore (_example)
        - Private: begin with a double underscore (__example)
    """
    
# super() => reference to the parent class
class A:
    def foo(self, x):
        print(x)
class B(A):
    def foo(self, x):
        super().foo(x)
            
# isinstance(o, T)  => check object o is of type T
class C: pass
class D(C): pass


if __name__ == '__main__':
    x = B()
    print(isinstance(x, B))    # True
    print(isinstance(x, A))    # True