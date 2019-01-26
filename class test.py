class Hello:
     def sayHello(self):
          print ("Hello world!")
 
hello1 = Hello()
hello1.sayHello()
 
hello2 = Hello()
hello2.sayHello()
class Hello:
     def __init__(self):
          print ("Constractor")
 
     def sayHello(self):
          print ("Hello world!")
 
hello1 = Hello()
hello1.sayHello()
 
hello2 = Hello()
hello2.sayHello()
class Hello:
     def __init__(self, name):
          self.n = name
 
def sayHello(self):
         return ("Hello " + self.n)
 
hello1 = Hello("Jack")
 
print (hello1.sayHello())
