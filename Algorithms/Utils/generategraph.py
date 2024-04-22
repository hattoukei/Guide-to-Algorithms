import random
import os.path


def generate_graph(min, max):
  random_num = random.randint(min, max)
  print(f"generating graph with {random_num - min + 1} nodes. range: {min} to {random_num}")
  new_graph = {i:{random.randint(min, random_num) for j in range(random.randint(1, random_num))} for i in range(min, random_num)}
  return new_graph

def save_graph(graph):
  current_path = os.path.abspath(os.path.dirname(__file__))
  target_path = os.path.join(current_path, "../Tests/randomgraph.txt")

  with open(target_path, "w") as file:
    file.write(str(graph))

def main():
  graph = {}
  graph = generate_graph(1, 100)
  print(graph)
  save_graph(graph)
  
main()