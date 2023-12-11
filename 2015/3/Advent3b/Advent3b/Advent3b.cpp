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
	int verti = 0;
	int horiz = 0;
	int horizo = 0;
	string temp;
	bool btemp = true;
	int x = 1;
	int g = 0;

	ifstream in("input.txt");

	while (in.peek() != EOF)
	{
		in >> letter;
		if (letter == '<')
		{
			if (g % 2 == 0)horiz--;
			else horizo--;
		}
		if (letter == '>')
		{
			if (g % 2 == 0)horiz++;
			else horizo++;
		}
		if (letter == 'v')
		{
			if (g % 2 == 0)vert--;
			else verti--;
		}
		if (letter == '^')
		{
			if (g % 2 == 0)vert++;
			else verti++;
		}
		g++;
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
		temp = to_string(horizo) + "," + to_string(verti);
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