#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int sex, age;
    cin >> sex >> age;
    if (age >= 19){
        if (sex == 0) {
            cout << "MAN";
        } else {
            cout << "WOMAN";
        }
    } else {
        if (sex == 0) {
            cout << "BOY";
        } else {
            cout << "GIRL";
        }
    }
    return 0;
}