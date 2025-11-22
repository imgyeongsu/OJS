#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int x;
    for (int i = 0; i < 3; i++){
        for (int j=0; j<3; j++){
            cin >> x;
            cout << x*3 << ' ';  
        }
        cout << '\n';
    }
    return 0;
}