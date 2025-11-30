#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int m;
    cin >> m;
    m = m % 12;
    if (m <= 2){
        cout << "Winter";
    } else if ( m <= 5) {
        cout << "Spring";
    } else if ( m <= 8) {
        cout << "Summer";
    } else if ( m <= 11) {
        cout << "Fall";
    }
    return 0;
}