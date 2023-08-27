#include <iostream>
#include <unordered_map>
#include <chrono>

class Timer {
public:
    Timer(const std::string &name) : m_name(name), m_start(std::chrono::high_resolution_clock::now()) {}

    ~Timer() {
        auto end = std::chrono::high_resolution_clock::now();
        auto duration = std::chrono::duration<double>(end - m_start).count();
        std::cout << "Result of " << m_name << " (execution time " << duration << "s)" << std::endl;
    }

private:
    std::string m_name;
    std::chrono::high_resolution_clock::time_point m_start;
};

long long P114(int L = 101) {
    std::unordered_map<int, long long> mem;

    auto add = [&](int l, long long count, int m) -> long long {
        if (mem.find(l) != mem.end()) return count + mem[l];
        for (int l0 = 0; l0 <= l - m; ++l0) {
            for (int ln = m; ln <= l - l0; ++ln) {
                count++;
                if (l - (ln + l0 + 1) >= m) {
                    count = add(l - (ln + l0 + 1), count, 3);
                }
            }
        }
        return count;
    };

    for (int l = 4; l <= L; ++l) {
        mem[l] = add(l, 0, 3);
    }

    return mem[L] + 1;
}

int main() {
    {
        Timer timer("P114");
        std::cout << "P114(L=50) = " << P114(50) << std::endl;
    }
    return 0;
}
