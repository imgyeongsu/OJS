#include <iostream>
using namespace std;

void score(int s){
    if (s >= 90){
        cout << "A ";
    } else if ( s>= 80) {
        cout << "B ";
    } else if ( s >= 70) {
        cout << "C ";
    } else if ( s >= 60) {
        cout << "D ";
    } else {
        cout << "F ";
    }
}

int main() {
    // Please write your code here.
    int n;
    cin >> n;
    while (n<101) {
        score(n);
        n ++ ;
    }
    return 0;
}