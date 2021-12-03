#include <fstream>
#include <iostream>
#include <limits>
#include <numeric>
#include <string>
#include <vector>

int count_increase(std::vector<int> vec, bool part2) {
    int increased = 0;
    int stride = (part2 == true) ? 3 : 1;
    int prev_sum = INT_MAX;

    for (size_t i = 0; i != vec.size() - 1; i++) {
        int j = stride + i;
        std::vector<int> subvec(&vec[i],&vec[j]);
        int the_sum = accumulate(subvec.begin(), subvec.end(), 0);

        if (the_sum > prev_sum) {
            increased++;
        }
        prev_sum = the_sum;
    }
    return increased;
}

int main() {
    std::ifstream infile;
    std::vector<int> measurements;
    std::string m;

    infile.open("inputs/01.txt");
    while (getline(infile, m)) {
        measurements.push_back(std::stoi(m));
    }
    infile.close();

    int solution1 = count_increase(measurements, false);
    std::cout << "The solution to part 1 is " << solution1 << std::endl;
    int solution2 = count_increase(measurements, true);
    std::cout << "The solution to part 2 is " << solution2 << std::endl;
}