#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main()
{
	char temp;
	int pos = 0;
	int count = 0;
	int s = 0;
	ifstream in("Text.txt");
	while (in.peek() != EOF)
	{
		s++;
		temp = ' ';
		in >> temp;
		if (temp == '(')
		{
			pos++;
		}
		else if (temp == ')')
		{
			pos--;
		}
		if (pos < 0)
		{
			count = s;
			//goto HAPPY;
		}
	}
HAPPY:
	cout << s << endl;
	cout << count;
}