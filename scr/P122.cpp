#include <iostream>
#include <vector>
#include <chrono>
#include <algorithm>
#include <numeric>

template <typename Function>
auto timer(Function func) -> decltype(func()) {
    auto start = std::chrono::high_resolution_clock::now();
    auto result = func();
    auto end = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double> elapsed = end - start;
    std::cout << "Resultado: " << result << " (execution time " << elapsed.count() << "s)" << std::endl;
    return result;
}

int sum_chain(const std::vector<int>& L, int N, int suma_actual, int lenth_min, int length_actual) {
    for (int i = L.size() - 1; i >= 0; --i) {
        int l = L[i];
        int suma_actual_l = suma_actual + l;

        if (suma_actual_l > N) {
            continue;
        } else if (suma_actual_l == N && length_actual < lenth_min) {
            lenth_min = length_actual;
        } else if (suma_actual_l < N && length_actual < lenth_min) {
            std::vector<int> newL = L;
            if (std::find(L.begin(), L.end(), suma_actual_l) == L.end()) {
                newL.push_back(suma_actual_l);
            }
            lenth_min = sum_chain(newL, N, suma_actual_l, lenth_min, length_actual + 1);
        }
    }
    return lenth_min;
}

int P122(int M) {
    std::vector<int> results;
    for (int n = 1; n <= M; ++n) {
        results.push_back(sum_chain({1}, n, 0, 9999, 0));
    }
    return std::accumulate(results.begin(), results.end(), 0);
}

int main() {
    timer([&]() -> int {
        return P122(200);
    });
    return 0;
}
