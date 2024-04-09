class Node:
  def __init__(self, data):
    self.data = data
    self.prev = None
    self.next = None

class DoublyLinkedList:
  def __init__(self):
    self.head = None
    self.tail = None

  def insertAtHead(self, data):
    new_node = Node(data)

    if self.head is None:
      self.head = new_node
      self.tail = new_node
      return
    else:
      new_node.next = self.head
      new_node.prev = self.tail
      self.head.prev = new_node
      self.head = new_node

  # ALWAYS CASE O(1)
  def insertAtTail(self, data):
    new_node = Node(data)

    if self.head is None:
      self.head = new_node
      self.tail = new_node
      return
    
    else:
      new_node.next = self.head
      new_node.prev = self.tail
      self.tail.next = new_node
      self.tail = new_node

  # WORST CASE O(n)
  def insertAtIndex(self, data, index):
    if index == 0:
      self.insertAtHead(data)
      return

    new_node = Node(data)
    current_node = self.head
    current_index = 0

    while (current_node is not None and current_index + 1 is not index):
      current_index += 1
      current_node = current_node.next

    if current_node is not None:
      new_node.next = current_node.next
      new_node.prev = current_node
      current_node.next = new_node

    else:
      print("Index out of range.")

  def getHead(self):
    if self.head is not None:
      return self.head.data
    else:
      print("List is empty.")

  # ALWAYS CASE O(n)
  def getTail(self):
    if self.tail is not None:
      return self.tail.data
    else:
      print("List is empty.")
    
  # ALWAYS CASE O(n)
  def printNodes(self):
    current_node = self.head
    while (True):
      print(current_node.data, end=" ")
      current_node = current_node.next
      if current_node is self.head:
        break

    



    

    
    

    
    
