#Encapsulation
class name:
  def __init__(self):
    self.var1 = "Aadi"
    self.__var2 = "Man"
  def Private(self):
    print(self.__var2)
obj = name()
print(obj.var1)
obj.Private()
