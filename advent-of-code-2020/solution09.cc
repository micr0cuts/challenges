#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>

// TODOs for the future to make this better:
// create a data structure that resembles a set in Python so as not to store sums
// that are already in the valid_sums vector

typedef std::vector<int> vecInt;

vecInt calculate_sums(vecInt twentyfive_entries) {
    vecInt valid_sums;
    for(size_t i = 0; i != twentyfive_entries.size(); i++) {
        for(size_t j = 0; j != twentyfive_entries.size(); j++) {
            if (i != j) {
                valid_sums.push_back(twentyfive_entries[i] + twentyfive_entries[j]);
            }
        }
    }
    return valid_sums;
}

int part1(vecInt entries) {
    for (size_t i = 0; i != entries.size()-25; i++){
        vecInt::const_iterator first = entries.begin() + i;
        vecInt::const_iterator last = entries.begin() + i + 25;
        vecInt subvec(first, last);

        vecInt valid_sums = calculate_sums(subvec);

        if (std::find(valid_sums.begin(), valid_sums.end(), entries[i+25]) == valid_sums.end()) {
            int invalid_num = entries[i+25];
            std::cout << "The solution to part 1 is " << invalid_num << std::endl;
            return invalid_num;
        }
    }
}

void part2(vecInt entries, int num) {
    for (size_t i = 0; i != entries.size(); i++) {
        vecInt contiguous_nums;
        int acc = 0;
        contiguous_nums.push_back(entries[i]);
        acc += entries[i];
        for (size_t j = i + 1; j != entries.size(); j++) {
            acc += entries[j];
            if (acc == num) {
                contiguous_nums.push_back(entries[j]);
                auto minmax = std::minmax_element(contiguous_nums.begin(), contiguous_nums.end());
                int solution = *minmax.first + *minmax.second;
                std::cout << "The solution to part 2 is " << solution << std::endl;
                return;
            }
            else if (acc > num) {
                break;
            }
            else if (acc < num) {
                contiguous_nums.push_back(entries[j]);
            }
        }
    }
}

int main() {
    std::ifstream file;
    std::string line;
    vecInt entries;

    file.open("input09.txt");

    while (getline(file, line)) {
        entries.push_back(std::stol(line));
    }
    file.close();

    int invalid_num = part1(entries);
    part2(entries, invalid_num);
}
