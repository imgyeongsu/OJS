#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int temperate;
    cin >> temperate;
    if (temperate < 0){
        cout << "ice";
    } else if (temperate < 100){
        cout << "water";
    } else {
        cout << "vapor";
    }
    return 0;
}