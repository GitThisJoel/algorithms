#include <iostream>
#include <string>
#include <vector>
#include <set>

using namespace std;

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(NULL);

	string in, prev, curr;
	cin >> in;
	int N = stoi(in); // nbr of iterations
	if (N == 0 || N == 1) {
		cout << "Fair Game";
		return 0;
	}
	else {
		cin >> prev;
	}

	set<string> words;
	words.insert(prev);
	int i = 0;
	while (cin >> curr) {
		if (prev[prev.length() - 1] != curr[0] || words.find(curr) != words.end()) {
			if (i % 2 == 0) {
				cout << "Player 2 lost";
				return 0; 
			}
			else {
				cout << "Player 1 lost";
				return 0;
			}
		}
		words.insert(curr);
		i++;
		prev = curr;
		if (i + 1 == N) {
			cout << "Fair Game";
			return 0;
		}
	}

	cout << "Fair Game";
	return 0;
}
