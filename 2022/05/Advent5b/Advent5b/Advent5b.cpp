#include <iostream>
#include <string>
#include <fstream>
using namespace std;

string order = "";

void doSomeStuff()
{
    string contents = "";

    ifstream in("input.txt");

    string s1 = "ftclrpgq";
    string s2 = "nqhwrfsj";
    string s3 = "fbhwpmq";
    string s4 = "vstdf";
    string s5 = "qldwvfz";
    string s6 = "zcls";
    string s7 = "zbmvdf";
    string s8 = "tjb";
    string s9 = "qnbglsph";
    string str[] = { s1, s2, s3, s4, s5, s6, s7, s8, s9 };

    while (in) {
        getline(in, contents);
        if (contents == "") {

        }
        else
        {
            int num = 0;
            string sinfo1 = "";
            string sinfo2 = "";
            string sinfo3 = "";
            string temp = "";
            int info1 = 0;
            int info2 = 0;
            int info3 = 0;
            for (int x = 0; x < contents.length(); x++)
            {
                if (num == 1 && contents[x] != ' ') {
                    sinfo1 += contents[x];
                }
                if (num == 3 && contents[x] != ' ') {
                    sinfo2 += contents[x];
                }
                if (num == 5) {
                    sinfo3 += contents[x];
                }
                if (contents[x] == ' ') {
                    num++;
                }
            }
            info1 = stoi(sinfo1);
            info2 = stoi(sinfo2);
            info3 = stoi(sinfo3);

            
            temp = str[info2 - 1].substr(str[info2 - 1].length() - info1, info1);
            str[info3 - 1] += temp;
            str[info2 - 1] = str[info2 - 1].substr(0, str[info2 - 1].length() - info1);
            
        }

        if (!in) {
            in.close();
        }
    }
    for (int x = 0; x < size(str); x++)
    {
        cout << str[x] << endl << endl;
        order += str[x][str[x].length() - 1];
    }
}

int main()
{
    doSomeStuff();
    cout << order << endl;
    system("pause");
}
