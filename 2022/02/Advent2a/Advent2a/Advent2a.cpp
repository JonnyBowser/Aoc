#include <iostream>
#include <string>
#include <fstream>
using namespace std;

int score = 0;

void doSomeStuff()
{
    string pair = "";
    
    ifstream in("input.txt");

    while (in) {
        getline(in, pair);
        if (pair == "") {

        }
        else
        {
            if (pair[2] == 'X') {
                score += 1;
                if (pair[0] == 'A') score += 3;
                if (pair[0] == 'B') score += 0;
                if (pair[0] == 'C') score += 6;
            }
            if (pair[2] == 'Y') {
                score += 2;
                if (pair[0] == 'A') score += 6;
                if (pair[0] == 'B') score += 3;
                if (pair[0] == 'C') score += 0;
            }
            if (pair[2] == 'Z') {
                score += 3;
                if (pair[0] == 'A') score += 0;
                if (pair[0] == 'B') score += 6;
                if (pair[0] == 'C') score += 3;
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
    cout << score << endl;
    system("pause");
}