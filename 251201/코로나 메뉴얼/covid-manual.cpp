#include <iostream>
#include <utility>
#include <vector>
using namespace std;

int main() {
    // Please write your code here.
    int cnt = 0;

    int t ;
    char c;
    for (int i = 0; i < 3; i++){
        cin >> c >> t;
        if (t >= 37 && c=='Y'){
            cnt ++;
        }
    }
    
    if (cnt >= 2){
        cout <<'E';
    } else {
        cout << 'N';
    }


    return 0;
}