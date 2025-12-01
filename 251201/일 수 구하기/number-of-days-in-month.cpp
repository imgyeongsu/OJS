#include <iostream>
#include <set>
using namespace std;

int main() {
    // Please write your code here.
    set<int> arr31 = {1,3,5,7,8,10,12};
    int n;
    cin >> n;
    if (arr31.count(n)){
        cout << "31";
    } else if ( n == 2) {
        cout << "28";
    } else {
        cout << "30";
    }
    return 0;
}