class SLLQueue:
  class Node:
    def __init__(self, data: object) -> None:
      self.data = data
      self.next = None

  def __init__(self) -> None:
    self.head = None
    self.tail = None
    self.n = 0

  def enqueue(self, data: object):
    new_node = self.Node(data)
    if self.n == 0:
      self.head = new_node
    else:
      self.tail.next = new_node
    self.tail = new_node
    self.n += 1 
    return True
  
  def dequeue(self) -> object:
    if self.n <= 0:
      raise IndexError
    if self.n == 0:
      return None
    data = self.head.data
    self.head = self.head.next
    self.n -= 1
    if self.n == 0:
      self.tail = None
    return data
  
  def size(self) -> int:
    return self.n
  
  def __str__(self):
    string = "["
    node = self.head
    while node is not None:
      string += "%r" % node.data
      node = node.next
      if node is not None:
        string += ","
    return string + "]"

  def __iter__(self):
    self.iterator = self.head
    return self

  def __next__(self):
    if self.iterator != None:
      data = self.iterator.data
      self.iterator = self.iterator.next
    else:
      raise StopIteration()
    return data

  



