#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int n;
    cin >> n;
    for (int i=1; i<6; i++){
        printf("%d%c", n*i, ' ');
    }
    return 0;
}