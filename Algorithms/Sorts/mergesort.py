import os.path
import filecmp

def merge(left, right):
  list = []

  i = 0
  j = 0

  while i < len(left) and j < len(right):
    if left[i] <= right[j]:
      list.append(left[i])
      i += 1
    elif left[i] > right[j]:
      list.append(right[j])
      j += 1

  while i < len(left):
    list.append(left[i])
    i += 1
  while j < len(right):
    list.append(right[j])
    j += 1

  return list


def merge_sort(nums):

  if len(nums) <= 1:
    return nums
  
  middle = len(nums) // 2
  left = merge_sort(nums[middle:])
  right = merge_sort(nums[:middle])

  return merge(left, right)

  


def main():
  current_path = os.path.abspath(os.path.dirname(__file__))
  path1 = os.path.join(current_path, "../Tests/numbers.txt")
  with open(path1) as file:
    nums = []
    for number in file.readlines():
      nums.append(int(number))
  file.close()

  sort = merge_sort(nums)

  path2 = os.path.join(current_path, "../Tests/sortednumbers2.txt")
  with open(path2, "w") as file:
    for number in sort:
      file.write(str(number))
      file.write("\n")
  file.close()

  sorted_path = os.path.join(current_path, "../Tests/sortednumbers.txt")


  if(filecmp.cmp(sorted_path, path2)):
    print("Sorted file matches the base case!")
  else:
    print("Sorted file doesn't match the base case.")


if __name__ == "__main__":
  main()
