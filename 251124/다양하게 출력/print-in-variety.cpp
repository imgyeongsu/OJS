#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    string msg1 = "Total days in Year";
    string msg2 = "365";
    string msg3 = "Circumference rate";
    string msg4 = "3.1415926535";
    
    string arr[4] = {msg1, msg2, msg3, msg4};
    
    for (int i =0; i<4; i++){
        cout << arr[i] << '\n';
    }

    return 0;
}