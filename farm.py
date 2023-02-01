class Animal:

  
  def __init__(self, name, age, position):
    self.name= name
    self.age=age
    self.position=position
  
  def __str__(self):
    return f"{self.name} is in the farm"
  
  def walking(self,increment):
    self.position = self.position + increment
    return self.position
  

miles=Animal("miles",7,100)
miles.walking(10)
