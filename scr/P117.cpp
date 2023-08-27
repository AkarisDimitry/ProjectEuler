#include <iostream>
#include <unordered_map>
#include <chrono>

using namespace std;

/* timer class to measure the execution time of functions */
class Timer {
public:
    Timer(const string& functionName) : start(chrono::high_resolution_clock::now()), funcName(functionName) {}
    ~Timer() {
        auto end = chrono::high_resolution_clock::now();
        auto duration = chrono::duration_cast<chrono::milliseconds>(end - start).count();
        cout << "Resultado of " << funcName << " : " << result << " (execution time " << duration << "ms)" << endl;
    }

    long long result;
private:
    chrono::time_point<chrono::high_resolution_clock> start;
    string funcName;
};

long long add(int l, long long count, unordered_map<int, long long>& mem, int m) {
    if (mem.find(l) != mem.end()) {
        return count + mem[l];
    } else {
        for (int l0 = 0; l0 <= l - m; l0++) {
            for (int ln = m; ln <= min(4, l - l0); ln++) {
                count++;
                if (l - (ln + l0) >= m) {
                    count = add(l - (ln + l0), count, mem, m);
                }
            }
        }
    }
    return count;
}

long long P117(int L = 50, int M = 3) {
    Timer timer("P117"); // Start timer

    unordered_map<int, long long> mem;
    for (int l = 0; l <= L; l++) {
        long long ans = add(l, 0, mem, 2);
        mem[l] = ans;
        if (ans + 1 > 1e20) break;
    }

    timer.result = mem[L] + 1;
    return timer.result;
}

int main() {
    cout << P117(50) << endl;
    return 0;
}
/* Resultado of P117 : 100808458960497 (execution time 2ms)
100808458960497 */

