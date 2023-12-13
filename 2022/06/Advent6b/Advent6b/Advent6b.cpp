#include <iostream>
#include <string>
#include <fstream>
using namespace std;

int num = 0;

bool askIfSame(string s)
{
    for (int x = 1; x < s.length(); x++)
    {
        if (s[0] == s[x])
        {
            return false;
        }
    }
    if (s.length() > 2)
    {
        if (askIfSame(s.substr(1, s.length() - 1)))
        {
            return true;
        }
        return false;
    }
    return true;
}

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
            for (int x = 0; x < contents.length() - 13; x++)
            {
                if (askIfSame(contents.substr(x, 14)))
                {
                    num = x + 14;
                    return;
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
