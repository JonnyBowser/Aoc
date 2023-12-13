#include <iostream>
#include <string>
#include <fstream>
using namespace std;

int sum = 0;

void doSomeStuff()
{
    string contents = "";
    int split = 0;
    int match = 0;

    ifstream in("input.txt");

    while (in) {
        getline(in, contents);
        if (contents == "") {

        }
        else
        {
            split = contents.length() / 2;
            for (int i = 0; i < split; i++)
            {
                for (int x = 0; x < split; x++)
                {
                    if (contents[i] == contents[split + x])
                    {
                        match = contents[i];
                        break;
                    }
                }
            }
            if (match > 96 && match < 123)
            {
                match -= 96;
            } else
            if (match > 64 && match < 91)
            {
                match -= 38;
            }
            sum += match;
        }

        if (!in) {
            in.close();
        }
    }
}

int main()
{
    doSomeStuff();
    cout << sum << endl;
    system("pause");
}