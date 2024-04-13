#include <iostream>
#include <fstream>
#include <time.h>
#include <array>

using namespace std;

int main()
{
  ifstream nums("../../Tests/sortednumbers.txt");
  const int size = 10000;

  int c = 0;
  int num;
  int *array = new int[size];

  while (nums >> num && c < size)
  {
    array[c++] = num;
  }

  for (int i; i < 100; i++)
  {
    cout << array[i] << endl;
  }

  nums.close();

  srand(time(0));

  int min = -20000;
  int max = 20000;

  num = (rand() % (max - min + 1)) + min;

  cout << "Searching for number '" << num << "'." << endl;

  bool found = false;
  int count;

  for (int i; i < size; i++)
  {
    if (array[i] == num)
    {
      found = true;
      count = i + 1;
      break;
    }

    continue;
  }

  if (found)
  {
    cout << "Number found in " << count << " tries.";
  }
  else
  {
    cout << "Number not found.";
  }

  return 0;
}