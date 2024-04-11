from stack import Stack

def main():
  stack = Stack()
  for i in range(20):
    stack.push(i)
  
  for i in range(3):
    stack.pop()

  stack.display()

  print(stack.peek())

  for i in range(20):
    stack.pop()

main()