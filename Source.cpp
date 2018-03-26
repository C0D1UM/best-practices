#include <iostream>;
#include <string>;
using namespace std;



void fizzBuzz() {
	for (int i = 1; i <= 100; i++) {
		if (i % 3 == 0 || i % 5 == 0) {
			if (i % 3 == 0 && i % 5 == 0) {
				cout << "FizzBuzz";
			}
			else {
				if (i % 3 == 0) {
					cout << "Fizz";
				}
				if (i % 5 == 0) {
					cout << "Buzz";
				}
			}
		}
		else {
			cout<<i;
		}
	}
}
void isLeapYear() {
	long year;
	try {
		cout << "Input number to determine if LeapYear:";
		cin >> year;
		if ((year % 400 == 0) || (year % 100 != 0 && year % 4 == 0)) {
			cout << "true";
		}
		else {
			cout << "false";
		}
	}
	catch(exception ex){ cout << "false"; }
}

void intOut_1(int n) {
	for (int i = 0; i < n; i++) {
		string out = "";
		for (int x = 0; x < i; x++)
			out += "*";
		if (i > 0)
			cout << out << endl;
	}
}
void intout_2(int n) {
	for (int x = 0; x < n; x++) {
		string space = "";
		string out = "";
		for (int i = 0; i < n - x; i++)
			space += " ";
		for (int i = 0; i < x; i++)
			out += "*";
		if (x > 0)
			cout << space + out << endl;
	}
}
void intout_3(int n) {
	for (int x = 0; x < n; x++) {
		string out = "";
		for (int i = 0; i <= x; i++) {
			
			if (i == 0 || i == x)
				out += "*";
			else
				out += " ";
		}
		cout << out << endl;
	}
}

int main() {
	int questionToLoad;
	cout << "Input question:";
	cin >> questionToLoad;
	switch (questionToLoad)
	{
	case 1:
		fizzBuzz();
		break;
	case 2:
		isLeapYear();
		break;
	case 3:
	{
		int section;
		int n;
		cout << "Which section in the 3rd Question to load:";
		cin >> section;
		cout << "Value of n:";
		cin >> n;
		switch (section) {
		case 1:
			intOut_1(n);
			break;
		case 2:
			intout_2(n);
			break;
		case 3:
			intout_3(n);
			break;
		default:
			break;
		}
	}
	default:
		break;
	}
}