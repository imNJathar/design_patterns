"""
Types of Design patterns
1) Creational DP
2) Structural DP
3) Behavioral DP
"""

"""
Pattern Name - SingleTon DP (mono state pattern)
Pattern Type - Creational DP

Description - In singleTon Design pattern only one object get server, if developer user tries to create 
new object and if it already exits it will return that otherwise will create new 
"""

# Solution 2


class Borg(object):
    _shared = {}

    def __init__(self) -> None:
        self.__dict__ = self._shared

class Singleton(Borg):
    def __init__(self, arg) -> None:
        print("In init")
        Borg.__init__(self)
        self.val = arg

obj1 = Singleton('Nikhil')
print(obj1)
print(obj1.val)

obj2 = Singleton('Rahul')
print(obj2)
print(obj2.val)
print(obj2.val)
