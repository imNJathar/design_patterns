"""
Types of Design patterns
1) Creational DP
2) Structural DP
3) Behavioral DP
"""

"""
Pattern Name - SingleTon DP
Pattern Type - Creational DP

Description - In singleTon Design pattern only one object get server, if developer user tries to create 
new object and if it already exits it will return that otherwise will create new 
"""

# Solution 1

class Singleton(object):
    def __new__(cls, *args, **kwargs):
        print("In new")
        if not hasattr(cls, "_instance"):
            cls._instance = super().__new__(cls, *args, *kwargs)
        return cls._instance

    def __init__(self) -> None:
        print("In init")
        super().__init__()


obj1 = Singleton()
print(obj1)
obj1.data = 10
print(obj1.data)

obj2 = Singleton()
print(obj2)
obj1.data = 20
print(obj2.data)
