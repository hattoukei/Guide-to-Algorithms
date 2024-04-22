from stack import Stack

def isValid(expression: str):
  hashmap = {')' : '(', '}' : '{', ']' : '['}
  stack = Stack()
  for x in expression:
    if x in hashmap.values():
      stack.push(x)
    else:
      if x in hashmap:
        if hashmap[x] == stack.peek():
          stack.pop()
        else: 
          return False
      
  return (stack.length() == 0)


def main():
  stack = Stack()
  for i in range(20):
    stack.push(i)
  
  stack.display()
  
  for i in range(3):
    stack.pop()

  stack.display()

  print(stack.peek())

  for i in range(20):
    stack.pop()

  map = {'a' : 'b'}
  if 'a' in map:
    print("yes")
  else:
    print("no")

  file = open("/Users/tensofu/Desktop/VSC/Guide-to-Algorithms/Data-Structures/Stacks/text.txt", "r")
  expressions = [x for x in file.readlines()]

  for x in expressions:
    print(isValid(x))

  file.close()



main()