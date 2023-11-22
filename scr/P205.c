#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>

// Function to calculate frequency of sums
void calculateFrequency(int numDice, int sides, int* frequency) {
    int maxOutcome = pow(sides, numDice);
    for (int i = 0; i < maxOutcome; i++) {
        int sum = 0, temp = i;
        for (int j = 0; j < numDice; j++) {
            sum += temp % sides + 1;
            temp /= sides;
        }
        frequency[sum]++;
    }
}

// Function to calculate probability distribution
void calculateProbabilityDistribution(int numDice, int sides, double* probabilityDistribution) {
    int frequency[sides * numDice + 1];
    memset(frequency, 0, sizeof(frequency));
    calculateFrequency(numDice, sides, frequency);

    int totalOutcomes = pow(sides, numDice);
    for (int i = numDice; i <= sides * numDice; i++) {
        probabilityDistribution[i] = (double)frequency[i] / totalOutcomes;
    }
}

// Main function to calculate probability
double P205() {
    clock_t start, end;
    double cpu_time_used;

    start = clock();

    double peterDistribution[37] = {0};
    double colinDistribution[37] = {0};

    calculateProbabilityDistribution(9, 4, peterDistribution);
    calculateProbabilityDistribution(6, 6, colinDistribution);

    double peterBeatsColinProbability = 0.0;

    for (int i = 9; i <= 36; i++) {
        double colinProbSum = 0.0;
        for (int j = 6; j < i; j++) {
            colinProbSum += colinDistribution[j];
        }
        peterBeatsColinProbability += peterDistribution[i] * colinProbSum;
    }

    end = clock();
    cpu_time_used = ((double) (end - start)) / CLOCKS_PER_SEC;

    printf("Execution time: %f seconds\n", cpu_time_used);

    return peterBeatsColinProbability;
}

int main() {
    double result = P205();
    printf("Probability that Pyramidal Peter beats Cubic Colin: %.7f\n", result);
    return 0;
}
