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
            count++;
            if (l - (m + l0) >= m) {
                count = add(l - (m + l0), count, mem, m);
            }
        }
    }
    return count;
}

long long P116(int L = 50, int M = 3) {
    Timer timer("P116"); // Start timer

    unordered_map<int, long long> mem2, mem3, mem4;

    for (int l = 0; l <= L; l++) {
        long long ans = add(l, 0, mem2, 2);
        mem2[l] = ans;
        if (ans + 1 > 1e20) break;
    }

    for (int l = 0; l <= L; l++) {
        long long ans = add(l, 0, mem3, 3);
        mem3[l] = ans;
        if (ans + 1 > 1e20) break;
    }

    for (int l = 0; l <= L; l++) {
        long long ans = add(l, 0, mem4, 4);
        mem4[l] = ans;
        if (ans + 1 > 1e20) break;
    }

    for (const auto& pair : mem2) {
        cout << pair.first << ": " << pair.second << ", ";
    }
    cout << endl;

    timer.result = mem2[L] + mem3[L] + mem4[L];
    return timer.result;
}

int main() {
    cout << P116(50, 2) << endl;
    return 0;
}
/* '''
50: 20365011073, 49: 12586269024, 48: 7778742048, 47: 4807526975, 46: 2971215072, 45: 1836311902, 44: 1134903169, 43: 701408732, 42: 433494436, 41: 267914295, 40: 165580140, 39: 102334154, 38: 63245985, 37: 39088168, 36: 24157816, 35: 14930351, 34: 9227464, 33: 5702886, 32: 3524577, 31: 2178308, 30: 1346268, 29: 832039, 12: 232, 11: 143, 10: 88, 9: 54, 8: 33, 7: 20, 6: 12, 5: 7, 4: 4, 3: 2, 2: 1, 1: 0, 0: 0, 13: 376, 14: 609, 15: 986, 16: 1596, 17: 2583, 18: 4180, 19: 6764, 20: 10945, 21: 17710, 22: 28656, 23: 46367, 24: 75024, 25: 121392, 26: 196417, 27: 317810, 28: 514228, 
Resultado of P116 : 20492570929 (execution time 2ms)
20492570929
''' */