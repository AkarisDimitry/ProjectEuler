#include <stdio.h>
#include <stdbool.h>
#include <math.h>
#include <string.h>
#include <stdlib.h>

// Struct to simulate the behavior of a C++ set with basic functionalities.
typedef struct {
    long long* data;   // Dynamic array to store unique values.
    int size;          // Current size of the set.
    int capacity;      // Total allocated memory for the set.
} Set;

// Function to create a set with a given initial capacity.
// Time Complexity: O(1)
// Space Complexity: O(capacity)
Set* create_set(int capacity) {
    Set* set = (Set*) malloc(sizeof(Set));
    set->data = (long long*) malloc(capacity * sizeof(long long));
    set->size = 0;
    set->capacity = capacity;
    return set;
}



// Function to insert a value into the set. 
// If the value is already present, it's not added again.
// Time Complexity: O(size) due to searching for duplicates.
// Space Complexity: O(1), but can be O(size) during resizing.
void insert(Set* set, long long value) {
    for (int i = 0; i < set->size; i++) {
        if (set->data[i] == value) {
            return;
        }
    }
    if (set->size == set->capacity) {
        set->capacity *= 2;
        set->data = (long long*) realloc(set->data, set->capacity * sizeof(long long));
    }
    set->data[set->size++] = value;
}

// Function to check if a value exists in the set.
// Time Complexity: O(size)
// Space Complexity: O(1)
bool contains(Set* set, long long value) {
    for (int i = 0; i < set->size; i++) {
        if (set->data[i] == value) {
            return true;
        }
    }
    return false;
}

// Function to free allocated memory for the set.
// Time Complexity: O(1)
// Space Complexity: O(1)
void destroy_set(Set* set) {
    free(set->data);
    free(set);
}

// Function to compute all possible sums of consecutive squares up to a given number N.
// Time Complexity: O(N) due to nested loops running up to sqrt(N).
// Space Complexity: O(N) due to the set's storage.
void squared_sum(int N, bool* sums) {
    int max_square = (int)sqrt(N) + 1;

    for (int n = 1; n < max_square; n++) {
        long long s = 0;
        for (int m = n; m < max_square; m++) {
            s += m * m;
            if (s > N) {
                break;
            }
            if (m > n) {
                sums[s] = true;
            }
        }
    }
}

// Function to check if a number is palindromic.
// Mathematically, a number is palindromic if its digits are the same when read forwards and backwards.
// Time Complexity: O(log(num)) due to iterating over digits.
// Space Complexity: O(log(num)) due to string representation storage.
bool is_palindrome(long long num) {
    long long original = num;
    long long reversed_num = 0;
    while (num) {
        reversed_num = reversed_num * 10 + num % 10;
        num /= 10;
    }
    return original == reversed_num;
}

// Main function to compute the sum of all numbers less than N that are both palindromic and can be written as the sum of consecutive squares.
// Time Complexity: O(N*log(N)) mainly due to generating sums and checking palindromic nature.
// Space Complexity: O(N) due to storing sums.

long long P125(int N) {
    bool* sums = (bool*)malloc((N + 1) * sizeof(bool));
    memset(sums, 0, (N + 1) * sizeof(bool));

    bool* palindrome_sums = (bool*)malloc((N + 1) * sizeof(bool));
    memset(palindrome_sums, 0, (N + 1) * sizeof(bool));

    squared_sum(N, sums);

    long long total = 0;
    for (int i = 0; i <= N; i++) {
        if (sums[i] && is_palindrome(i) && !palindrome_sums[i]) {
            total += i;
            palindrome_sums[i] = true;
        }
    }

    free(sums);
    free(palindrome_sums);

    return total;
}

int main() {
    printf("%lld\n", P125(100000000));
    return 0;
}