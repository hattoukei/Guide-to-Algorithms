import os.path
import random


def binary_search(nums, target):
  # Iterative approach.
  low = 0
  high = len(nums) - 1
  while low <= high:
    middle = (low + high) // 2
    if low == high and nums[middle] != target:
      return None
    if nums[middle] == target:
      return middle
    elif nums[middle] < target:
      low = middle + 1
    else: 
      high = middle - 1
  return None


def recursive_binary_search(nums, target):
  # Recursive approach.
  if len(nums) == 0:
    return False
  middle = len(nums) // 2
  if nums[middle] == target:
    return True
  else: 
    if nums[middle] < target:
      return recursive_binary_search(nums[middle + 1:], target)
    if nums[middle] > target:
      return recursive_binary_search(nums[:middle], target)
    
def search(nums, count, min, max):
  # Helper function to randomly generate `count` numbers in range `min` to `max`.
  for i in range(count):
    target = random.randrange(min, max)
    print(f"Searching for target: {target}.")
    print("Index:", binary_search(nums, target))
    print(recursive_binary_search(nums, target))

def main():
  current_path = os.path.abspath(os.path.dirname(__file__))
  path = os.path.join(current_path, "../../Tests/sortednumbers.txt")
  with open(path) as file:
    nums = []
    for number in file.readlines():
      nums.append(int(number))
  file.close()

  # Searches
  search(nums, 3, -20000, 20000)

if __name__ == "__main__":
  main()