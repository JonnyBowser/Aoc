#include <iostream>
#include <string>
#include <fstream>
using namespace std;

int coun = 0;

void doSomeStuff()
{
    string contents = "";
    string strnum1 = "";
    string strnum2 = "";
    string strnum3 = "";
    string strnum4 = "";
    int num1 = 0;
    int num2 = 0;
    int num3 = 0;
    int num4 = 0;

    ifstream in("input.txt");

    while (in) {
        getline(in, contents);
        if (contents == "") {

        }
        else
        {
            int x = 0;
            for (; x < contents.length(); x++)
            {
                if (contents[x] == '-') {
                    goto AFTER1;
                }
                strnum1 += contents[x];
            }
        AFTER1:
            for (x++; x < contents.length(); x++)
            {
                if (contents[x] == ',') {
                    goto AFTER2;
                }
                strnum2 += contents[x];
            }
        AFTER2:
            for (x++; x < contents.length(); x++)
            {
                if (contents[x] == '-') {
                    goto AFTER3;
                }
                strnum3 += contents[x];
            }
        AFTER3:
            for (x++; x < contents.length(); x++)
            {
                strnum4 += contents[x];
            }
            num1 = stoi(strnum1);
            num2 = stoi(strnum2);
            num3 = stoi(strnum3);
            num4 = stoi(strnum4);

            if ((num1 <= num3 && num2 >= num4) || (num3 <= num1 && num4 >= num2))
            {
                coun++;
            }

            strnum1 = "";
            strnum2 = "";
            strnum3 = "";
            strnum4 = "";

        }

        if (!in) {
            in.close();
        }
    }
}

int main()
{
    doSomeStuff();
    cout << coun << endl;
    system("pause");
}
