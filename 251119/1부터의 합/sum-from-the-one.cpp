#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int n;
    cin >> n;
    int total = 0;
    int i = 1;
    while (true) {
        total += i;
        if (total >= n){
            cout << i;
            break;
        }
        i++;
    }

    return 0;
}