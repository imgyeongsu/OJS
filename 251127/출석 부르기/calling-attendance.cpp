#include <iostream>
#include <map>
#include <string>
using namespace std;

int main() {
    // Please write your code here.
    int i;
    cin >> i;
    map<int, string> m;
    m.insert({1, "John"});
    m.insert({2, "Tom"});
    m.insert({3, "Paul"});
    cout << m.at(i);
    return 0;
}