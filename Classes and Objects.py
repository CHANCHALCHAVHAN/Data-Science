#########################################################################################
#A blueprint for  creating  objects 
class Circle:
    def __init__(self,x,y,r):
        self.x=x
        self.y=y
        self.r = r
        
    def circumference(self):
        return 2*3.14*self.r
        
    def area(self):
        return 3.14*self.r*self.r 
        
#creating an object of circle
a_circle=Circle(2.0,2.0,1.0)
b_circle=Circle(3.0,3.0,2.0)

#accesing data and metods 
print("radius:",a_circle.r)
print("circumference:",a_circle.circumference())
print("area:",a_circle.area())

print("radius:",b_circle.r)
print("circumference:",b_circle.circumference())
print("area:",b_circle.area())

#constructor is needed to create a object of the class
#########################################################################################
#Encapsulations
#hiding internal data by making it private class
class Circle:
    def __init__(self,x,y,r):
        self.__x= x
        self.__y= y 
        self.__r= r
        
        
    def get_radius(self):
        return self.__r 
        
    def set_radius(self,r):
        if r>0:
            self.__r=r
        else:
            print("invalid radius")
                
#usage
c2=Circle(1,1,1)
print(c2.get_radius())

#########################################################################################
#Inheritance
class Circle:
    def __init__(self,x,y,r):
        self.x=x
        self.y=y
        self.r = r
    def circumference(self):
        return 2*3.14*self.r
        
    def area(self):
        return 3.14*self.r**2
    
    def display_info(self):
        print(f"content:({self.x},{self.y}),Radius:{self.r}")
        print(f"Area: {self.area():.2f}")
        print(f"circumference:{self.circumference():.2f}")
        
        
#derived class
class ColoredCircle(Circle):
    def __init__(self,x,y,r,color):
        super().__init__(x,y,r)
        self.color=color
        
        #overiding the display _info method
    def display_info(self):
        super().display_info()
        print(f"color: {self.color}")
            
c1=ColoredCircle(0,0,5,"red")
c1.display_info()

#########################################################################################
#polymorphism
class Circle:
    def area(self):
        return "calculating area of circle"

class square:
    def area(self):
        return "calculating area of square"
    
#usage
shapes=[Circle(),square()]
for shape in shapes:
    print(shape.area())

#########################################################################################
#Abstraction
#hiding complex logic and showing essential features using abstarct class
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def greet(self):
        print(f"hello my name is {self.name} and i am {self.age} years old")
            
#object
person1=person("chanchal",19)
person1.greet()

class Bankacount:
    def __init__(self,balance):
        self.__balance=balance
    def deposit(self,amount):
        if amount>0:
            self.__balance+=amount
    
    def get_balance(self):
        return self.__balance
    
ba1=Bankacount(300)
print(ba1.get_balance())
ba1.deposit(100)
print(ba1.get_balance())
