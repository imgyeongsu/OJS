#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    string a;
    cin >> a;
    a[1] = 'a';
    a[a.length()-2] = 'a';
    cout << a;


    return 0;
}