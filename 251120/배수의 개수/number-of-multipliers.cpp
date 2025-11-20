#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int n;
    int multiple3 = 0;
    int multiple5 = 0;
    for (int i = 0; i < 10; i++){
        cin >> n;
        if (n % 3 ==0){
            multiple3 ++;
        }
        if (n % 5){
            multiple5 ++;
        }
    }
    cout << multiple3 << ' ' << multiple5;
    
    return 0;
}