class SLLStack:
  class Node:
    def __init__(self, data: object) -> None:
      self.data = data
      self.next = None

  def __init__(self) -> None:
    self.head = None
    self.tail = None
    self.n = 0

  def push(self, data: object):
    new_node = self.Node(data)
    new_node.next = self.head
    self.head = new_node
    if self.n == 0:
      self.tail = new_node
    self.n += 1

  def pop(self):
    if self.n <= 0:
      return IndexError
    if self.n == 0:
      return None
    data = self.head.data
    self.head = self.head.next
    self.n -= 1
    if self.n == 0:
      self.tail = None
    return data
  
  def peek(self):
    return self.head.data
  
