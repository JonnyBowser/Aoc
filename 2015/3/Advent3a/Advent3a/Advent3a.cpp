#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main()
{
	int solution = 0;

	char letter;
	string contents;
	int count = 0;
	string santa[8500];
	santa[0] = "0,0";
	int vert = 0;
	int horiz = 0;
	string temp;
	bool btemp = true;
	int x = 1;

	ifstream in("input.txt");

	while (in.peek() != EOF)
	{
		in >> letter;
		if (letter == '<')
		{
			horiz--;
		}
		if (letter == '>')
		{
			horiz++;
		}
		if (letter == 'v')
		{
			vert--;
		}
		if (letter == '^')
		{
			vert++;
		}
		temp = to_string(horiz) + "," + to_string(vert);
		for (int i = 0; i < size(santa); i++)
		{
			if (santa[i] == temp)
			{
				btemp = false;
			}
		}
		if (btemp)
		{
			santa[x] = temp;
			x++;
		}
		btemp = true;
	}
	for (int x = 0; x < size(santa); x++)
	{
		if (santa[x] != "")
		{
			count++;
		}
	}

	cout << count;
}