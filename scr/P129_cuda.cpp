/*
A number consisting entirely of ones is called a repunit. We shall
define R(k) to be a repunit of length k; for example, R(6) = 111111.
Given that n is a positive integer and gcd(n, 10) = 1, it can 
be shown that there always exists a value, k, for which R(k) is 
divisible by n, and let A(n) be the least such value of k; for 
example, A(7) = 6 and A(41) = 5.
The least value of n for which A(n) first exceeds ten is 17.
Find the least value of n for which A(n) first exceeds one-million.
*/

#include <iostream>
#include <cuda_runtime.h>
#include <chrono>

const int THREADS_PER_BLOCK = 512;

__global__ void computeA(int N, int *results) {
    int n = blockIdx.x * blockDim.x + threadIdx.x + N/10 - 1000;
    
    if (n < N && n % 2 != 0 && n % 5 != 0) {
        int k = 2;
        int res = 11;
        int res0 = 10;

        while (res != 0) {
            res0 = (res0 * 10) % n;
            res = (res0 + res) % n;
            k++;
        }
        
        results[n - N/10 + 1000] = k;
    }
}

int main() {
    int N = 10000000;
    int size = N - N/10 + 1000;
    int *d_results, *h_results;

    h_results = new int[size];
    cudaMalloc(&d_results, size * sizeof(int));

    auto start = std::chrono::high_resolution_clock::now();

    computeA<<<(size + THREADS_PER_BLOCK - 1) / THREADS_PER_BLOCK, THREADS_PER_BLOCK>>>(N, d_results);
    cudaMemcpy(h_results, d_results, size * sizeof(int), cudaMemcpyDeviceToHost);

    auto stop = std::chrono::high_resolution_clock::now();

    int maxValue = 0;
    for (int i = 0; i < size; i++) {
        if (h_results[i] > 1000000) {
            maxValue = i + N/10 - 1000;
            break;
        }
    }

    auto duration = std::chrono::duration_cast<std::chrono::milliseconds>(stop - start);

    std::cout << "Result: " << maxValue << " (execution time " << duration.count()/1000.0 << " seconds)" << std::endl;

    delete[] h_results;
    cudaFree(d_results);
    
    return 0;
}
