#include <iostream>
#include <string>
#include <fstream>
using namespace std;

int num = 0;

void doSomeStuff()
{
    string contents = "";

    ifstream in("input.txt");

    while (in) {
        getline(in, contents);
        if (contents == "") {

        }
        else
        {
            for (int x = 0; x < contents.length() + 3; x++)
            {
                if (contents[x] != contents[x + 1] && contents[x] != contents[x + 2] && contents[x] != contents[x + 3])
                {
                    if (contents[x + 1] != contents[x + 2] && contents[x + 1] != contents[x + 3])
                    {
                        if (contents[x + 2] != contents[x + 3])
                        {
                            num = x + 4;
                            return;
                        }
                    }
                }
            }
        }

        if (!in) {
            in.close();
        }
    }
}

int main()
{
    doSomeStuff();
    cout << num << endl;
    system("pause");
}
