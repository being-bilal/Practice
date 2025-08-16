
#include <iostream>
using namespace std;

int main() {
    // F = \frac{9}{5} \times C + 32
    double temp;
    cout << "Enter temprature in degrees : " << endl;
    cin >> temp;
    double ftemp =((9.0/5.0) * temp) + 32.0;
    cout << "temprature in fahrenheit : " << ftemp << endl;

    return 0;
}