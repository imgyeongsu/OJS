#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int N;
    cin >> N;
    if ((N % 3 == 0 && N % 2 == 1) || (N % 10 == 0)){
        cout << "true";
    } else {
        cout << "false";
    }
    return 0;
}