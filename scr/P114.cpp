#include <iostream>
#include <unordered_map>
#include <chrono>

using namespace std;

// Timer class to measure the execution time of functions
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
            for (int ln = m; ln <= l - l0; ln++) {
                count++;

                if (l - (ln + l0 + 1) >= m) {
                    count = add(l - (ln + l0 + 1), count, mem, 3);
                }
            }
        }
    }
    return count;
}

long long P114(int L = 101) {
    Timer timer("P114"); // Start timer

    unordered_map<int, long long> mem;
    for (int l = 4; l <= L; l++) {
        long long ans = add(l, 0, mem, 3);
        mem[l] = ans;
    }

    timer.result = mem[L] + 1;
    return timer.result;
}

int main() {
    cout << P114(50) << endl;
    return 0;
}
/*'''
Resultado of P114 : 16475640049 (execution time 7ms)
16475640049
''' */