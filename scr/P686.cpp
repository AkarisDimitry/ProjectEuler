#include <iostream>
#include <cmath>
#include <ctime>

/*
C++ and C are quite similar, especially for simpler programs. However, there are a few differences:

In C++, we use the iostream library for input and output, and the using namespace std; directive to avoid having to prefix everything with std::.
The C++ code uses cout for output instead of printf.
The type casting in C++ is done with the static_cast operator.
You can compile and run the code using a C++ compiler like g++:
*/

using namespace std;

long long pe686(long long target) {
    double upper_limit = log10(1.24);
    double lower_limit = log10(1.23);
    double n = log10(pow(2, 196));
    double m = log10(pow(2, 93));  // 289 - 196
    double x = log10(pow(2, 12710));
    long long i = 12710;
    long long nth = 45;

    while (nth < target) {
        x += n;
        i += 196;
        double d = fmod(x, 1.0);

        if (d > lower_limit && d < upper_limit) {
            nth++;
            continue;
        }
        
        x += m;
        i += 93;
        d = fmod(x, 1.0);
        
        if (d > lower_limit && d < upper_limit) {
            nth++;
        }
    }

    return i;
}

int main() {
    clock_t start_time, end_time;

    start_time = clock();
    long long result = pe686(678910);
    end_time = clock();

    double elapsed_time = static_cast<double>(end_time - start_time) / CLOCKS_PER_SEC;
    cout << "pe686 took " << elapsed_time << " seconds to run." << endl;
    cout << "Output: " << result << endl;

    return 0;
}

/*
g++ filename.cpp -o outputname -lm
./outputname
*/