#include <iostream>
#include <cstdlib>
#include <fstream>

using namespace std;

void swap_num(int &a, int &b)
{
    int temp = a;
    a = b;
    b = temp;
}

void bubbleSort(int array[], int n)
{
    for (int j = 0; j < n - 1; j++)
    {
        for (int i = 0; i < n - 1 - j; i++)
        {
            if (array[i] > array[i + 1])
            {
                swap_num(array[i], array[i + 1]);
            }
        }
    }
}

int main()
{
    fstream nums("numbers.txt");
    fstream out("sortednumbers.txt");
    const int size = 10000;

    int c = 0;
    int num;
    int array[size];

    while (nums >> num && c < size)
    {
        array[c++] = num;
    }

    nums.close();
    cout << array[70] << endl;

    bubbleSort(array, c);

    for (int i = 0; i < c; i++)
    {
        out << array[i] << endl;
    }

    out.close();

    return 0;
}