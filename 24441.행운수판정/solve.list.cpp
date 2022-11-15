#include <bits/stdc++.h>
using namespace std;

#include "lucky.h"

int main() {
    ios::sync_with_stdio(0); cin.tie(0);
    
    int T; cin >> T;
    while (T--) {
        int n; cin >> n;
        if (binary_search(lucky, lucky+LEN_LUCKY, n))
            cout << "lucky" << "\n";
        else
            cout << "unlucky" << "\n";
    }
}