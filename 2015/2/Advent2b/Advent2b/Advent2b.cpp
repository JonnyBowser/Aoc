#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main()
{
	char letter;
	string contents;

	ifstream in("input.txt");

	int solution = 0;

	string s1;
	string s2;
	string s3;
	int n1;
	int n2;
	int n3;
	int num = 0;
	while (in.peek() != EOF)
	{
		getline(in, contents);
		for (int x = 0; x < contents.length(); x++)
		{
			if (contents[x] == 'x')
			{
				num++;
			}
			else if (num == 0)
			{
				s1 += contents[x];
			}
			else if (num == 1)
			{
				s2 += contents[x];
			}
			else if (num == 2)
			{
				s3 += contents[x];
			}
		}

		n1 = stoi(s1);
		n2 = stoi(s2);
		n3 = stoi(s3);

		if (n1 >= n2 && n1 >= n3)
		{
			solution += 2 * (n2 + n3);
		}
		else if (n2 >= n3)
		{
			solution += 2 * (n1 + n3);
		}
		else
		{
			solution += 2 * (n1 + n2);
		}

		solution += n1 * n2 * n3;

		num = 0;
		s1 = "";
		s2 = "";
		s3 = "";
	}

	cout << solution;
}