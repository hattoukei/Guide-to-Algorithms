#include <iostream>
#include <fstream>
#include <cstdlib>
#include <time.h>

using namespace std;

int main(int argc, char *argv[])
{
  int num;

  if (argc != 4)
  {
    cout << "You need three arguments" << endl;
    return 1;
  }

  int count = stoi(argv[1]);
  int min = stoi(argv[2]);
  int max = stoi(argv[3]);

  ofstream clean;
  clean.open("numbers.dat", ofstream::out | ofstream::trunc);
  clean.close();

  fstream outp("numbers.dat");

  srand(time(0));
  for (int i = 0; i < count; i++)
  {
    num = (rand() % (max - min + 1)) + min;
    outp << num << endl;
  }

  outp.close();

  return 0;
};