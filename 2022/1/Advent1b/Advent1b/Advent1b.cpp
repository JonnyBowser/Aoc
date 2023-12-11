#include <iostream>
#include <string>
#include <fstream>
using namespace std;

int max1 = 0;
int max2 = 0;
int max3 = 0;

void doSomeStuff()
{
    int num = 0;
    int sum = 0;
    string numstr = "";
    //reading information from input file
    ifstream in("input.txt");
    while (in) {
        getline(in, numstr);
        if (numstr == "") {
            if (sum > max1) {
                max3 = max2;
                max2 = max1;
                max1 = sum;
            }
            else if (sum > max2) {
                max3 = max2;
                max2 = sum;
            }
            else if (sum > max3) {
                max3 = sum;
            }
            sum = 0;
        }
        else {
            num = stoi(numstr);
            sum += num;
        }
        if (!in) {
            in.close();
        }
    }
}

int main()
{
    doSomeStuff();
    cout << max1 << endl << max2 << endl << max3 << endl;
    cout << max1 + max2 + max3 << endl;
    system("pause");
}