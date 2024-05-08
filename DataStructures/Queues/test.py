from queue import Queue
from SLLQueue import SLLQueue

def main():
  queue = SLLQueue()
  for i in range(20):
    queue.enqueue(i)

  print(queue)
  
  for i in range(3):
    queue.dequeue()

  print(queue)

  for i in range(15):
    queue.dequeue()

  print(queue)

main()