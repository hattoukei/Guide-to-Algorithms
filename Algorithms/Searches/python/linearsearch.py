import os.path
import random

def linear_search(nums, target):
  print(f"Searching for target: {target}.")
  count = 0
  for number in nums:
    if number == target:
      print(f"Target found in {count + 1} tries.")
      return
    count += 1
  print("Target was not found.")

def main():
  current_path = os.path.abspath(os.path.dirname(__file__))
  path = os.path.join(current_path, "../../Tests/sortednumbers.txt")
  with open(path) as file:
    nums = []
    for number in file.readlines():
      nums.append(int(number))
  file.close()

  for i in range(10):
    target = random.randrange(-20000, 20000)
    linear_search(nums, target)

main()