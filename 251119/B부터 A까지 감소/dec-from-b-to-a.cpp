#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int a, b;
    cin >> a >> b;
    b++;
    while(b-->a){
        printf("%d%c", b, ' ');
    }
    return 0;
}