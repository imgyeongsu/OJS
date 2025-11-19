#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int a , b;
    cin >> a >> b;
    int hap = 0;
    for (int i = a; i < b+1; i++){
        if (i % 2 == 0) {
            hap += i;
        }
    }
    cout << hap;
    return 0;
}