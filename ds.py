class Stack():
  def __init__(self,a):
    self.data=[a]
  def push (self,a):
    self.data.append(a)
  def popout(self):
    self.data=self.data[0:-1]
  def printdata (self):
    print(*self.data)