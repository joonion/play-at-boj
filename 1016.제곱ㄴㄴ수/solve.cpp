#include <bits/stdc++.h>
using namespace std;

typedef unsigned long long long_t;

int solve(long_t n, long_t m) {
    vector<bool> sieve(m - n + 1, true);
    for (long_t k = 2; k * k <= m; k++) {
        long_t s = k * k;
        long_t i = (s - (n % s)) % s;
        for (long_t j = i; j < sieve.size(); j += s)
            sieve[j] = false;
    }
    int cnt = 0; 
    for (int i = 0; i < sieve.size(); i++)
        if (sieve[i]) cnt++;
    return cnt;
}

int main() {
    long_t n, m; cin >> n >> m;
    cout << solve(n, m);
}