#include <iostream>
#include <vector>
#include <map>
#include <chrono>

using namespace std;
using namespace std::chrono;

// Function to generate all possible outcomes of rolling dice
vector<int> rollDice(int numDice, int sides) {
    vector<int> outcomes;
    int maxOutcome = pow(sides, numDice);
    for (int i = 0; i < maxOutcome; i++) {
        int sum = 0, temp = i;
        for (int j = 0; j < numDice; j++) {
            sum += temp % sides + 1;
            temp /= sides;
        }
        outcomes.push_back(sum);
    }
    return outcomes;
}

// Function to calculate the probability distribution
map<int, double> calculateProbabilityDistribution(int numDice, int sides) {
    vector<int> outcomes = rollDice(numDice, sides);
    map<int, int> frequency;
    map<int, double> probabilityDistribution;

    for (int sum : outcomes) {
        frequency[sum]++;
    }

    int totalOutcomes = outcomes.size();
    for (auto& p : frequency) {
        probabilityDistribution[p.first] = (double)p.second / totalOutcomes;
    }

    return probabilityDistribution;
}

// Timer decorator equivalent in C++
double P205() {
    auto start = high_resolution_clock::now();

    // Calculate probability distribution for Peter (9 four-sided dice)
    map<int, double> peterDistribution = calculateProbabilityDistribution(9, 4);

    // Calculate probability distribution for Colin (6 six-sided dice)
    map<int, double> colinDistribution = calculateProbabilityDistribution(6, 6);

    double peterBeatsColinProbability = 0.0;

    for (auto& peter : peterDistribution) {
        double colinProbSum = 0.0;
        for (auto& colin : colinDistribution) {
            if (colin.first < peter.first) {
                colinProbSum += colin.second;
            }
        }
        peterBeatsColinProbability += peter.second * colinProbSum;
    }

    auto stop = high_resolution_clock::now();
    auto duration = duration_cast<microseconds>(stop - start);
    cout << "Execution time: " << duration.count() << " microseconds" << endl;

    return round(peterBeatsColinProbability * 10000000) / 10000000.0;
}

int main() {
    double result = P205();
    cout << "Probability that Pyramidal Peter beats Cubic Colin: " << result << endl;
    return 0;
}
