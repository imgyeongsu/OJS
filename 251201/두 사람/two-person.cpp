#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int a1,a2;
    char s1, s2;
    cin >> a1 >> s1 >> a2 >> s2;
    if ((a1 >= 19 && s1 == 'M')|| (a2>=19 && s2 =='M')){
        cout << 1;
    } else {
        cout << 0;
    }
    return 0;
}