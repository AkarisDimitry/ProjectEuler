#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

bool is_pandigital(long long n) {
    std::string s = std::to_string(n);
    std::sort(s.begin(), s.end());
    return s == "123456789";
}

int main() {
    long long f1 = 1, f2 = 1;
    long long f1_m9 = 1, f1_M9 = 1, f2_m9 = 1, f2_M9 = 1;
    int idx = 2;
    while (idx < 2000000) {
        // Update the Fibonacci numbers
        long long temp = f2;
        f2 = f1 + f2;
        f1 = temp;
        // Update the first 20 digits
        f1_m9 = f2_m9;
        f2_m9 = f1_m9 + f2_m9;
        if (f2_m9 > 1e20) f2_m9 = stoll(to_string(f2_m9).substr(0, 20));
        // Update the last 9 digits
        f1_M9 = f2_M9;
        f2_M9 = f1_M9 + f2_M9;
        if (f2_M9 > 1e9) f2_M9 = stoll(to_string(f2_M9).substr(to_string(f2_M9).size() - 9, 9));
        idx++;
        if (is_pandigital(f2_M9)) {
            if (is_pandigital(stoll(to_string(f2_m9).substr(0, 9)))) {
                std::cout << idx << " " << f2_m9 << " " << f2_M9 << std::endl;
                break;
            }
        }
    }
    return 0;
}