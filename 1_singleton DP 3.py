"""
Types of Design patterns
1) Creational DP
2) Structural DP
3) Behavioral DP
"""

"""
Pattern Name - SingleTon DP (Using decorator)
Pattern Type - Creational DP

Description - In singleTon Design pattern only one object get server, if developer user tries to create 
new object and if it already exits it will return that otherwise will create new 
"""

# Solution 3

class decorLogger(object):
    def __init__(self, LoggerClass) -> None:
        self.LoggerClass = LoggerClass
        self.instance = None

    def __call__(self, *args, **kwds):
        if not self.instance:
            self.instance = self.LoggerClass(*args, **kwds)
        return self.instance

@decorLogger
class Logger():
    def __init__(self) -> None:
        self.start = None

    def write(self, message):
        if self.start:
            print(self.start, message)
        else:
            print(message)


obj1 = Logger()
obj1.start = "> "
obj1.write("There is error")
print(obj1)

obj2 = Logger()
obj2.write("There is another error")
print(obj2)