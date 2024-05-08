from ..Queues.SLLQueue import SLLQueue

class BinaryTree:
  """Binary Tree with properties and traversals.
    depth (int): refers to the amount of EDGES the TARGET node is from the root.
    height (int): refers to the amount of EDGES of the FARTHEST node from the root.
  """

  class Node:
    def __init__(self, key = None, value = None) -> None:
      self.parent, self.left, self.right = None
      self.key = key
      self.value = value

    def set_key(self, key):
      self.key = key

    def set_value(self, value):
      self.value = value

    def insert_left(self, new_node: object):
      self.left = new_node
      self.left.parent = self
      return self.left
    
    def insert_right(self, new_node: object):
      self.right = new_node
      self.right.parent = self
      return self.right
    
    def __str__(self):
      return f"({self.key}:{self.value})"
    
  def __init__(self):
    """Defines the root node (has no parent)"""
    self.root = None

  def depth(self, node: Node) -> int:
    """Searches for an EXISTING Node in the tree, then counts its way up until it reaches the root."""
    if node is None:
      return -1
    depth = 0
    current_node = node
    while current_node != self.root:
      current_node = current_node.parent
      depth += 1
    return depth
  
  def height(self) -> int:
    return self._height(self.root)

  def _height(self, node: Node) -> int:
    """Recursively calls on itself and the node's children.
      This works because when you hit a leaf, the function returns 0 (since it has no children), then adds it to
      all of the recursive returns.
    """
    if node is None:
      return -1
    return 1 + max(self._height(node.left), self._height(node.right))
  
  def size(self) -> int:
    return self._size(self.root)

  def _size(self, node: Node) -> int:
    """Recursively calls on itself and the node's children.
      If the node does not exist (i.e. children of leaves), adds 0 and no more calls are made for that path.
      Otherwise, recursively adds 1 per node met, adding it as you backtrack.
    """
    if node is None:
      return 0
    return 1 + self._size(node.left) + self._size(node.right)
  
  def bf_order(self):
    """Breadth First Traversal: Returns a list of nodes from left to right horizontally, before vertically traversing downwards (traverses CLOSEST LEVELS first).
      Works since you use the queue to determine which nodes to look at in order.
      By first enqueueing ALL available children of the parent node, you are guaranteed to cover ALL nodes that share the same depth.
      Then, as you start dequeueing and appending those nodes, you start enqueueing their children (which also all share the same depth)
      This way, you GUARANTEE that parent nodes are appended before their children, and when done left to right, it is a breadth first search.
    """
    nodes = []
    queue = SLLQueue()
    if self.root is not None:
      queue.enqueue(self.root)
    while queue.size() > 0:
      node = queue.dequeue
      nodes.append(node)
      if node.left is not None:
        queue.enqueue(node.left)
      if node.right is not None:
        queue.enqueue(node.right)
    return nodes
  
  def in_order(self) -> list:
    return self._in_order(self.root)
  
  def _in_order(self, node: Node) -> list:
    """In-order Traversal: Visits the tree in LEFT-PARENT-RIGHT order."""
    nodes = []
    if node.left is not None:
      nodes.extend(self._in_order(node.left))
    nodes.append(node)
    if node.right is not None:
      nodes.extend(self._in_order(node.right))
    return nodes
  
  def post_order(self) -> list:
    return self._post_order(self.root)
  
  def _post_order(self, node: Node) -> list:
    """In-order Traversal: Visits the tree in LEFT-RIGHT-PARENT order."""
    nodes = []
    if node.left is not None:
      nodes.extend(self._post_order(node.left))
    if node.right is not None:
      nodes.extend(self._post_order(node.right))
    nodes.append(node)
    return nodes
  
  def pre_order(self) -> list:
    return self._pre_order(self.root)
  
  def _pre_order(self, node: Node) -> list:
    """In-order Traversal: Visits the tree in LEFT-RIGHT-PARENT order."""
    nodes = []
    nodes.append(node)
    if node.left is not None:
      nodes.extend(self._pre_order(node.left))
    if node.right is not None:
      nodes.extend(self._pre_order(node.right))
    return nodes
  
  def __str__(self):
    nodes = self.bf_order()
    nodes_str = [str(node) for node in nodes]
    return ', '.join(nodes_str)

    





