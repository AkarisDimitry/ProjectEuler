#include <iostream>
#include <algorithm>
#include <cmath>
#include <string>

bool is_pandigital(long long n) {
    std::string s = std::to_string(n);
    std::sort(s.begin(), s.end());
    return s == "123456789";
}

int main() {
    long long mod = 1000000000;
    long long f1 = 1, f2 = 1;
    double log_f1 = 0, log_f2 = std::log10(f1);
    int idx = 2;

    while (true) {
        long long temp = f2;
        f2 = (f1 + f2) % mod;
        f1 = temp;

        double temp_log = log_f2;
        log_f2 = log_f2 + log_f1 - int(log_f1);
        log_f1 = temp_log;

        idx++;
        if (is_pandigital(f2)) {
            long long first_9_digits = std::pow(10, log_f2 - int(log_f2) + 8);
            if (is_pandigital(first_9_digits)) {
                break;
            }
        }
    }

    std::cout << idx << std::endl;

    return 0;
}