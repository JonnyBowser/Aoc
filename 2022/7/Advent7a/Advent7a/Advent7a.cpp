#include <iostream>
#include <string>
#include <fstream>
#include <vector>
using namespace std;

int num = 0;

int depth = 0;

void doSomeOtherStuff(int x)
{

}

void doSomeStuff()
{
    string contents = "";
    int size = 0;

    ifstream in("input.txt");

    while (in.peek() != EOF) {
        getline(in, contents);
        if (contents.substr(0, 4) == "$ cd") {
            if (contents.substr(5, 2) != "..")
            {

            }
            else
            {
                num += size;
                size = 0;
            }
        }
    }
    in.close();
}

int main()
{
    doSomeStuff();
    cout << num << endl;
    system("pause");
}
