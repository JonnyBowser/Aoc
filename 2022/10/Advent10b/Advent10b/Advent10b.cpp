#include <iostream>
#include <fstream>
#include <string>
using namespace std;

char disp[6][40];
int x = 1;
int y = 0;
int cyc = 0;
int temp = 0;


void dosmth()
{
	if (cyc % 40 == 0 && cyc != 0)
	{
		y++;
	}
	if (x - 1 == cyc % 40 || x == cyc % 40 || x + 1 == cyc % 40)
	{
		disp[y][cyc % 40] = '#';
	}
	else
	{
		disp[y][cyc % 40] = ' ';
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
		dosmth();
		cyc++;
		if (contents.substr(0, 1) == "a")
		{
			contents = contents.substr(5, contents.length() - 5);
			temp = stoi(contents);
			dosmth();
			cyc++;
			x += temp;
			temp = 0;
		}

	}
	for (int row = 0; row < 6; row++)
	{
		for (int col = 0; col < 40; col++)
		{
			cout << disp[row][col];
		}
		cout << endl;
	}
}