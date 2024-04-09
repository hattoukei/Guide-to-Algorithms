class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class SinglyLinkedList:
  def __init__(self):
    self.head = None

  # ALWAYS CASE O(1)
  def insertAtHead(self, data):
    new_node = Node(data)
    if self.head is None:
      self.head = new_node
      return
    else:
      new_node.next = self.head
      self.head = new_node
      return
    
  # ALWAYS CASE O(n)
  def insertAtTail(self, data):
    new_node = Node(data)
    if self.head is None:
      self.head = new_node
      return
    
    current_node = self.head
    while current_node.next:
      current_node = current_node.next

    current_node.next = new_node

  # WORST CASE O(n)
  def insertAtIndex(self, data, index):
    new_node = Node(data)
    current_node = self.head
    position = 0
    if position == index:
      self.insertAtHead(data)
      return
    
    while(current_node is not None and position + 1 != index):
      position += 1
      current_node = current_node.next

    if current_node is not None:
      new_node.next = current_node.next
      current_node.next = new_node

    else:
      print("Index out of range.")

  # ALWAYS CASE O(1)
  def getHead(self):
    if self.head is not None:
      return self.head.data
    else:
      print("List is empty.")

  # ALWAYS CASE O(n)
  def getTail(self):
    if self.head is None:
      print("List is empty.")
      return
    
    current_node = self.head
    while (current_node.next is not None):
      current_node = current_node.next

    return current_node.data

  # ALWAYS CASE O(n)
  def printNodes(self):
    current_node = self.head
    while current_node is not None:
      print(current_node.data, end=" ")
      current_node = current_node.next




    
  