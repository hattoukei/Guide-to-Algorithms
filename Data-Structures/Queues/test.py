from queue import Queue

def main():
  queue = Queue()
  for i in range(20):
    queue.push(i)

  queue.display()
  
  for i in range(3):
    queue.pop()

  queue.display()

  for i in range(20):
    queue.pop()

main()