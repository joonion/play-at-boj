#include <bits/stdc++.h>
using namespace std;

#include "lucky_map.h"

int main() {
    ios::sync_with_stdio(0); cin.tie(0);
    
    int T; cin >> T;
    while (T--) {
        unsigned int n; cin >> n;
        if ((lucky[n/32] & (0x80000000U >> (n%32))) == 0)
            cout << "unlucky" << "\n";
        else
            cout << "lucky" << "\n";
    }
}