#include <iostream>
#include <sstream>
#include <stack>
using namespace std;

int main() {
    int n;
    cin >> n;
    cin.ignore();

    while (n--) {
        string line;
        getline(cin, line);
        stringstream ss(line);

        stack<int> pila;
        bool paranormal = false;
        int x;

        while (ss >> x) {
            if (x > 0) {
                pila.push(x);
            } 
            else if (x < 0) {
                if (pila.empty() || pila.top() != -x) {
                    paranormal = true;
                    break;
                }
                pila.pop();
            }
        }

        
        if (!pila.empty()) paranormal = true;

        if (paranormal) {
            cout << "PARANORMAL\n";
        } 
        else { 
            cout << "NORMAL\n";
        } 
    }
}

