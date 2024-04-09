from singlylinkedlist import SinglyLinkedList
from doublylinkedlist import DoublyLinkedList

def testSinglyLinkedList():
  print("SinglyLinkedList Test:")
  list = SinglyLinkedList()
  for i in range(0, 25):
    list.insertAtTail(i)
  list.insertAtIndex("INSERT", 6)
  list.printNodes()
  print()
  print(f"Head: {list.getHead()}, Tail: {list.getTail()}.")

def testDoublyLinkedList():
  print("DoublyLinkedList Test:")
  list = DoublyLinkedList()
  for i in range(0, 25):
    list.insertAtTail(i)
  list.insertAtIndex("INSERT", 6)
  list.printNodes()
  print()
  print(f"Head: {list.getHead()}, Tail: {list.getTail()}.")

def main():
  print("--- TESTING LINKED LISTS ---")
  testSinglyLinkedList()
  testDoublyLinkedList()
  print()

main()