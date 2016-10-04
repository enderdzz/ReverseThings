#include <iostream>

using namespace std;

int a = 4;

int &f(int x){
	a = a + x;
	return a;
}

int main(){
	int t = 5;
	cout << f(t) << endl;
	f(t) = 20;
	cout << f(t) << endl;
	t = f(t);
	cout << f(t) << endl;
	return 0;
}
