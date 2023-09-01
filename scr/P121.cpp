#include <iostream>
#include <vector>
#include <algorithm>
#include <chrono>

using namespace std;
using namespace chrono;

// Función para calcular las combinaciones de un conjunto.
void combine(int start, int n, int k, vector<int>& current, vector<vector<int>>& result) {
    if (k == 0) {
        result.push_back(current);
        return;
    }
    for (int i = start; i <= n; i++) {
        current.push_back(i);
        combine(i + 1, n, k - 1, current, result);
        current.pop_back();
    }
}

// Función principal para resolver el problema.
int P121(int n, int m) {
    double prob = 0;

    for (int k = m; k <= n; k++) {
        vector<vector<int>> combinations;
        vector<int> current;
        combine(1, n, k, current, combinations);

        for (vector<int> combi : combinations) {
            double p_k = 1;

            for (int i : combi) {
                p_k *= 1.0 / (i + 1);
            }

            for (int i = 1; i <= n; i++) {
                if (find(combi.begin(), combi.end(), i) == combi.end()) {
                    p_k *= 1 - 1.0 / (i + 1);
                }
            }

            prob += p_k;
        }
    }

    return static_cast<int>(1.0 / prob);
}

int main() {
    int n = 15;
    int m = 8;

    auto start = high_resolution_clock::now();
    int result = P121(n, m);
    auto stop = high_resolution_clock::now();
    auto duration = duration_cast<microseconds>(stop - start);

    cout << "Resultado de P121: " << result << " (tiempo de ejecución " << duration.count() / 1e6 << "s)" << endl;

    return 0;
}
