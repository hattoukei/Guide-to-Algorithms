class Stack:
  def __init__(self):
    self.items = []

  def length(self):
    return len(self.items)

  def push(self, data):
    self.items.append(data)

  def pop(self):
    if (self.items):
      return self.items.pop()
    print("Stack is empty.")

  def peek(self):
    if (self.items):
      return self.items[-1]
    print("Stack is empty.")

  def display(self):
    print(self.items)