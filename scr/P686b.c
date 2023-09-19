#include <stdio.h>
#include <math.h>
#include <time.h>

// Function to measure the execution time of another function
double timeit(clock_t start_time, clock_t end_time) {
    double elapsed_time = ((double)(end_time - start_time)) / CLOCKS_PER_SEC;
    return elapsed_time;
}

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

    double elapsed_time = timeit(start_time, end_time);
    printf("pe686 took %.5f seconds to run.\n", elapsed_time);
    printf("Output: %lld\n", result);

    return 0;
}


/*
gcc filename.c -o outputname -lm
./outputname
*/