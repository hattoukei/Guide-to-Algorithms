class Stack:
  def __init__(self):
    self.stack = []

  def length(self):
    return len(self.stack)

  def push(self, data):
    self.stack.append(data)

  def pop(self):
    if (self.stack):
      return self.stack.pop()
    print("Stack is empty.")

  def peek(self):
    if (self.stack):
      return self.stack[-1]
    print("Stack is empty.")

  def display(self):
    print(self.stack)