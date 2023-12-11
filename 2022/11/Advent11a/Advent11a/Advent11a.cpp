#include <iostream>
#include <fstream>
#include <string>
#include <vector>
using namespace std;

class Monkey
{
private:
public:
	unsigned long long monkeyNumber;
	string monkeyOperation;
	unsigned long long monkeyTest;
	unsigned long long monkeyTrueThrow;
	unsigned long long monkeyFalseThrow;
	vector<unsigned long long>monkeyItems;
	unsigned long long monkeyCount = 0;
	//should be private but I'm lazy
	Monkey()
	{
		monkeyNumber = 0;
		monkeyOperation = "";
		monkeyTest = 0;
		monkeyTrueThrow = 0;
		monkeyFalseThrow = 0;
		monkeyCount = 0;
	}
	void setMNum(unsigned long long i);
	void setMOp(string str);
	void setMTes(string str);
	void setMTThr(string str);
	void setMFThr(string str);
	void setMIt(string str);
	void displayMonkey();
	void doTurn();
};

Monkey monkeys[8];

void fillMonkeyData(string temp)
{
	unsigned long long mNum;
	for (unsigned long long i = 0; i < temp.length(); i++)
	{
		if (temp[i] == 'M')
		{
			mNum = stoi(temp.substr(i + 7, 1));
			monkeys[mNum].setMNum(mNum);
		}
		if (temp[i] == 'S')
		{
			unsigned long long index = i;
			for (; temp[index] != '\n'; index++);
			monkeys[mNum].setMIt(temp.substr(i + 16, index - i - 16));
		}
		if (temp[i] == 'O')
		{
			unsigned long long index = i;
			for (; temp[index] != '\n'; index++);
			monkeys[mNum].setMOp(temp.substr(i + 21, index - i - 21));
		}
		if (temp[i] == 'T')
		{
			unsigned long long index = i;
			for (; temp[index] != '\n'; index++);
			monkeys[mNum].setMTes(temp.substr(i + 19, index - i - 19));
		}
		if (temp[i] == 'I')
		{
			if (temp[i + 3] == 't')
			{
				monkeys[mNum].setMTThr(temp.substr(i + 25, 1));
			}
			else
			{
				monkeys[mNum].setMFThr(temp.substr(i + 26, 1));
			}
		}
	}
}

void runRound()
{
	for (unsigned long long i = 0; i < size(monkeys); i++)
	{
		monkeys[i].doTurn();
	}
}

void Monkey::doTurn()
{
	while (!monkeyItems.empty())
	{
		monkeyCount++;
		if (monkeyOperation[0] == '+')
		{
			monkeyItems[0] += stoi(monkeyOperation.substr(2, monkeyOperation.length() - 2));
		}
		if (monkeyOperation[0] == '*')
		{
			if (monkeyOperation[2] == 'o')
			{
				monkeyItems[0] *= monkeyItems[0];
			}
			else
			{
				monkeyItems[0] *= stoi(monkeyOperation.substr(2, monkeyOperation.length() - 2));
			}
		}
		monkeyItems[0] %= 9699690;
		if (monkeyItems[0] % monkeyTest == 0)
		{
			monkeys[monkeyTrueThrow].monkeyItems.push_back(monkeyItems[0]);
		}
		else
		{
			monkeys[monkeyFalseThrow].monkeyItems.push_back(monkeyItems[0]);
		}
		monkeyItems.erase(monkeyItems.begin());
	}
}

unsigned long long findMax1()
{
	unsigned long long max1 = 0;
	unsigned long long max2 = 0;
	for (unsigned long long i = 0; i < size(monkeys); i++)
	{
		if (monkeys[i].monkeyCount > max1)
		{
			max2 = max1;
			max1 = monkeys[i].monkeyCount;
		}
		else if (monkeys[i].monkeyCount > max2)
		{
			max2 = monkeys[i].monkeyCount;
		}
	}
	return max1;
}

unsigned long long findMax2()
{
	unsigned long long max1 = 0;
	unsigned long long max2 = 0;
	for (unsigned long long i = 0; i < size(monkeys); i++)
	{
		if (monkeys[i].monkeyCount > max1)
		{
			max2 = max1;
			max1 = monkeys[i].monkeyCount;
		}
		else if (monkeys[i].monkeyCount > max2)
		{
			max2 = monkeys[i].monkeyCount;
		}
	}
	return max2;
}

int main()
{
	string contents;
	string temp;
	bool usefulbool = false;

	ifstream in("input.txt");

	while (in.peek() != EOF)
	{
		getline(in, temp);
		if (temp.substr(0, 1) == "M" && usefulbool)
		{
			fillMonkeyData(contents);
			contents = "";
		}
		usefulbool = true;
		contents += temp + "\n";
	}
	for (unsigned long long i = 0; i < size(monkeys); i++)
	{
		monkeys[i].displayMonkey();
	}
	for (unsigned long long i = 0; i < 20; i++)
	{
		runRound();
		for (unsigned long long i = 0; i < size(monkeys); i++)
		{
			monkeys[i].displayMonkey();
		}
	}
	cout << findMax1() * findMax2();
}

void Monkey::setMNum(unsigned long long i)
{
	monkeyNumber = i;
}

void Monkey::setMOp(string str)
{
	monkeyOperation = str;
}

void Monkey::setMTes(string str)
{
	monkeyTest = stoi(str);
}

void Monkey::setMTThr(string str)
{
	monkeyTrueThrow = stoi(str);
}

void Monkey::setMFThr(string str)
{
	monkeyFalseThrow = stoi(str);
}

void Monkey::setMIt(string str)
{
	string temp = "";
	for (unsigned long long i = 0; i < str.length(); i++)
	{
		if (str[i] == ',')
		{
			i += 2;
			monkeyItems.push_back(stoi(temp));
			temp = "";
		}
		temp += str[i];
	}
	if (temp == "") return;
	monkeyItems.push_back(stoi(temp));
}

void Monkey::displayMonkey()
{
	cout << "MonkeyNumber = " << monkeyNumber << endl
		<< "MonkeyItems = ";
	for (unsigned long long i = 0; i < monkeyItems.size(); i++)
	{
		cout << monkeyItems[i] << ", ";
	}
	cout << endl << "MonkeyOperation = " << monkeyOperation << endl
		<< "MonkeyTest = " << monkeyTest << endl
		<< "MonkeyTrueThrow = " << monkeyTrueThrow << endl
		<< "MonkeyFalseThrow = " << monkeyFalseThrow << endl
		<< "MonkeyCount = " << monkeyCount << "\n\n";
}
