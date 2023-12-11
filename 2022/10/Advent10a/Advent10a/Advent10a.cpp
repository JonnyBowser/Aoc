#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int x = 1;
int cyc = 0;
int temp = 0;
int total = 0;

void dosmth()
{
	if (cyc % 40 == 20)
	{
		cout << cyc << endl;
		total += x * cyc;
	}
}

int main()
{
	char letter;
	string contents;
	

	ifstream in("input.txt");

	while (in)
	{
		getline(in, contents);
		cyc++;
		dosmth();
		//cout << cyc << " - " << x << endl;
		if (contents.substr(0, 1) == "a")
		{
			contents = contents.substr(5, contents.length() - 5);
			temp = stoi(contents);
			cyc++;
			//cout << cyc << " - " << x << endl;
			dosmth();
			x += temp;
			temp = 0;
		}

	}
	cout << total;
}