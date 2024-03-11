class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()





class employee:
    def __init__(self, name, age, staffID, ):
        self.name = name
        self.age = age
        self.staffID = staffID

    def getstaffID(self):
        print("Hello my staffID is " + self.staffID)
        
employee1 = employee("John", 36,"83201")
employee1.getstaffID()