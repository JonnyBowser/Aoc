#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main()
{
	char temp;
	int count = 0;
	ifstream in("Text.txt");
	while (in)
	{
		temp = ' ';
		in >> temp;
		if (temp == '(')
		{
			count++;
		}
		else if (temp == ')')
		{
			count--;
		}
	}
	cout << count;
}