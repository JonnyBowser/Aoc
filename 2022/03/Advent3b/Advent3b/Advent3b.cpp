#include <iostream>
#include <string>
#include <fstream>
using namespace std;

int sum = 0;

void doSomeStuff()
{
    string contents = "";
    string str1 = "";
    string str2 = "";
    string str3 = "";
    int count = 0;
    int match = 0;

    ifstream in("input.txt");

    LOOP:while (in) {
        getline(in, contents);
        if (contents == "") {

        }
        else
        {
            count++;
            if ((count + 2) % 3 == 0) {
                str1 = contents;
            }
            else if ((count + 1) % 3 == 0) {
                str2 = contents;
            }
            else if (count % 3 == 0) {
                str3 = contents;
                for (int x = 0; x < str1.length(); x++)
                {
                    for (int y = 0; y < str2.length(); y++)
                    {
                        if (str1[x] == str2[y]) {
                            for (int z = 0; z < str3.length(); z++)
                            {
                                if (str1[x] == str3[z]) {
                                    match = str3[z];
                                    if (match > 96 && match < 123)
                                    {
                                        match -= 96;
                                    }
                                    else
                                        if (match > 64 && match < 91)
                                        {
                                            match -= 38;
                                        }
                                    sum += match;
                                    goto LOOP;
                                }
                            }
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
    cout << sum << endl;
    system("pause");
}