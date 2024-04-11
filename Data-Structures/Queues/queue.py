class Queue:
  def __init__(self):
    self.items = []

  def size(self):
    return len(self.items)
  
  def push(self, data):
    self.items.append(data)

  def pop(self):
    if (self.items):
      self.items.pop(0)
    else:
      print("queue is empty")

  def display(self):
    print(self.items)
    