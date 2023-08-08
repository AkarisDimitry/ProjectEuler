#include <iostream>
#include <vector>
#include <cmath>
#include <climits>

using namespace std;

int next(vector<int>& count, int maxcount) {
    int i = 0;
    while (i < count.size() && count[i] == maxcount) {
        i++;
    }
    if (i < count.size()) {
        int n = count[i];
        while (i >= 0) {
            count[i] = n + 1;
            i--;
        }
    } else {
        return -1;  // Retorna -1 en lugar de None
    }
    return 0;
}

long long getn(const vector<int>& primes, const vector<int>& count) {
    long long num = 1;
    for (int i = 0; i < count.size(); i++) {
        num *= pow(primes[i], count[i]);
    }
    return num;
}

double ways(const vector<int>& cfacts) {
    double i = 1.0;
    for (auto c : cfacts) {
        i *= 2.0 * c + 1.0;
    }
    return (i + 1.0) / 2.0;
}

int P110() {
    int cmax = 3;
    vector<int> primes = {
        2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41,
        43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97
    };
    vector<int> count(primes.size(), 0);

    long long nmin = LLONG_MAX;
    while (next(count, cmax) != -1) {
        long long num = getn(primes, count);
        if (num < nmin) {
            long long w = ways(count);
            if (w > 4000000) {
                nmin = num;
            }
        }
    }

    return nmin;
}

int main() {
    cout << P110() << endl;
    return 0;
}