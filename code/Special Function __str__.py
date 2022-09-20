#Special Function __str__

class Person:
    name=""

p=Person()
print(p) #prints some random value <__main__.Person object at 0x1096f38e0>

class Man:
    name=""
    def __str__(self):
        return "This message is instead of object memory random value when you try to print obj"

m=Man()
print(m) #prints 'This message is instead of object memory random value when you try to print obj'
