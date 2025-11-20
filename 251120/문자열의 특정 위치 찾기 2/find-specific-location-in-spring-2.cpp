#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    char c;
    cin >> c;
    string arr[5] = {"apple", "banana", "grape", "blueberry", "orange"};
    
    int cnt = 0;
    for (int i =0; i < 5; i++){
        if (arr[i][2] == c || arr[i][3]==c){
            cout << arr[i] << '\n';
            cnt ++;
        }
    }
    cout << cnt;

    return 0;
}