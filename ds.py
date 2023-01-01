class Stack():
  def __init__(self,a):
    self.data=[a]
  def push (self,a):
    self.data.append(a)
  def popout(self):
    self.data=self.data[0:-1]
  def printdata (self):
    print(*self.data)

class queue():
  def __init__(self,a):
    self.a=a
  def enqueue(self,elt):
    a.append(elt)
  def dequeue (self):
    self.a=self.a[1:]
