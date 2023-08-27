#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

std::vector<std::string> generate_numbers(int N, int n, int m) {
    std::vector<std::string> results;
    std::vector<int> digits = {0, 1, 3, 4, 5, 6, 7, 8, 9};
    digits.erase(std::remove(digits.begin(), digits.end(), n), digits.end());

    std::string base(N, 'x');
    for (int i = 0; i <= N - m; ++i) {
        for (int j = i; j <= N - m; ++j) {
            std::string current = base;
            current.replace(i, m, std::string(m, '0' + n));
            int remaining = N - m;
            for (int k = 0; k < digits.size(); ++k) {
                std::string temp = current;
                int pos = 0;
                for (int l = 0; l < remaining; ++l) {
                    while (temp[pos] != 'x') {
                        ++pos;
                    }
                    temp[pos] = '0' + digits[k];
                    ++pos;
                }
                results.push_back(temp);
            }
        }
    }
    return results;
}

int main() {
    int N = 4;
    int n = 2;
    int m = 2;
    std::vector<std::string> numbers = generate_numbers(N, n, m);
    for (const std::string& number : numbers) {
        std::cout << number << std::endl;
    }
    return 0;
}