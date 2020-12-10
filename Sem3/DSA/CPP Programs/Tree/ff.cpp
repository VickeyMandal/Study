#include <iostream>
#include <math.h>
using namespace std;

int main()
{
    double sum = 0, a;
    int n, i;
    cout << " Input the value for nth term: ";
    cin >> n;
    for (i = 1; i <= n; ++i) 
	{
        a = pow(i, i)/i;
        cout << a << endl;
        sum += a;
    }
    cout << " The sum : " << sum << endl;
}

