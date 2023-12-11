//Lab4 -- This program creates an output file and adds to it information about hotel rooms.
//CSCN 111-005
//Jonny Bowers

#include <iostream>
#include <string>
#include <fstream>
using namespace std;

int doSomeStuff()
{
    int num = 0;
    int sum = 0;
    int max = 0;
    string numstr = "";
    //reading information from input file
    ifstream in("input.txt");
    while (in) {
        getline(in, numstr);
        if (numstr == "") {
            sum = 0;
        }
        else {
            num = stoi(numstr);
            sum += num;
            if (sum > max) {
                max = sum;
            }
        }
        if (!in) {
            in.close();
        }
    }
    return max;
}

int main()
{
    cout << doSomeStuff() << endl;
    system("pause");
}